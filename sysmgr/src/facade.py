# -*- coding: utf-8 -*-
import connector, dao, sysmain, sysvars
import datetime, thread, time, xlwt
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from configer import Config

class Facade(QObject):
    sinOutMsg = pyqtSignal(str)
    
    #初始端口
    port = 8080
    
    #数据库地址
    database = None
    
    #应用实例
    app = None
    
    #登录信息
    #登录用户
    logonUser = ''
    #是否系统用户
    isAnonymouseUser = True
    #是否远程连接
    mode = 'none'
    
    #配置信息
    config = None
    
    def __init__(self):
        super(Facade, self).__init__() 
        pass
        
    def prepare_network(self, user=None, password=None, localOnly=False):
        self.connection = connector.FsConnection()

        #读取配置信息        
        self.msg('读取配系统置信息')
        self.config = Config(self)
        self.config.loadSysConfigFromIni()
        if user is None:
            self.config.loadUserFromIni()
        else:
            self.config.param['user'] = user
            self.config.param['password'] = password
        
        #读取远程路径
        remotepath = self.config.param['remotepath']
        #从第2个字符开始查找
        remotehost = remotepath[:remotepath.find('\\', 2)]
        
        
        
        #用户无保存信息
        if self.config.param['user'] == '': 
            user = self.config.param['sysuser']
            password = self.config.param['syspassword']
            self.isAnonymouseUser = True
        else:
            user = self.config.param['user']
            password = self.config.param['password']
            self.isAnonymouseUser = False 
        
        self.logonUser = user
        user_with_scope = self.config.param['scope'] + '\\' + user
        
        
        
        self.msg('开始检查网络')
        #在内网环境
        if not localOnly and self.connection.check_netuse(remotehost, user_with_scope, password):
            self.database = remotepath.decode('gbk').encode('utf-8')
            self.mode = 'remote'
            self.msg('已连接目标网络，使用远程数据库{0}'.format(self.database))
        else:
            self.database = self.config.param['localpath']
            self.mode = 'local'
            self.msg('使用本地数据库{0}'.format(self.database))
            
        dao._DATABASE = self.database
        return self.mode
    
    #使用多线程启动服务器
    def start_server_async(self):
        self.msg('正在检查可用端口')
        self.port = self.connection.check_port()
        
        self.msg('正在启动服务,端口{0}'.format(self.port))
        thread.start_new_thread(self.thread_startserver, (1, 1))  
        pass
    
    def thread_startserver(self, no, interval):
        #初始化全局变量
        if self.mode == 'remote':
            sysvars._LOGIN_USER = self.logonUser
            sysvars._EDITABLE = True
        else:
            sysvars._LOGIN_USER = '匿名用户'
            sysvars._EDITABLE = False
        sysvars._MODE = self.mode
        
        self.app = sysmain.SysmgrApp(sysmain.urls, globals())
        self.app.run(port=self.port)
    
    #检查数据库是否能够正常访问
    def checkDatabase(self):
        try:
            db = dao.Database()
            version = db.getGlobalVersion()
            return True, version
        except Exception, ex:
            print ex
            return False, {}
    
    #输出日志
    def msg(self, text):
        strMsg = unicode('{0} {1}'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                  , unicode(str(text))))
        print strMsg
        
        try:
            f = open('log.txt', 'a')
            f.write(strMsg + '\n')
            f.close()
        except Exception, ex:
            strMsg = strMsg + '\r\n' + unicode(str(ex)) 

        try:
            strShortMsg = strMsg[11:]
            self.sinOutMsg.emit(strShortMsg)
        except:
            pass
    
    #导出文件
    def export2excel(self, filename):
#        localpath = self.config.param['localpath']
#        db = dao.Database(localpath)

        db = dao.Database()
        cols = db.getCols()
        
        #构造查询字符串
        col_str = ','.join([u'{0} as {1}'.format(r[1], r[0]) for r in cols])
        sql = 'select ' + col_str + ' from systable'
#        print sql
        rows = db.select(sql)
        
        font0 = xlwt.Font()
        font0.name = 'Times New Roman'
        font0.colour_index = 2
        font0.bold = True

        style0 = xlwt.XFStyle()
        style0.font = font0
        
#        style1 = xlwt.XFStyle()
#        style1.num_format_str = 'D-MMM-YY'
        
        wb = xlwt.Workbook()
        ws = wb.add_sheet(u'系统信息')
        
#        model = sysmodel.model()
        
        #写表头
        for i in range(len(cols)):
            ws.write(0, i, cols[i][1])

        #写内容
        for j in range(len(rows)):
            for i in range(len(cols)):
                ws.write(j + 1, i, rows[j][i])
        
        wb.save(filename)
        self.msg(u'已导出文件到: ' + filename)
    
    #同步远程文件到本地
    def synchronizeDatabase(self, localpath=None):
        if localpath is None:
            self.connection.copyFile(self.config.param['remotepath'], self.config.param['localpath'])
        else:
            self.connection.copyFile(self.config.param['remotepath'], localpath)
        

class FacadeThread(QThread):
    
    sinOutLogin = pyqtSignal(str)
    sinOutAppStart = pyqtSignal()
    sinOutExport = pyqtSignal()
    sinOutFail = pyqtSignal(str)
    
    
    def __init__(self, fs, parent=None):
        super(FacadeThread, self).__init__(parent)
        self.facade = fs
        self.action = ''
        self.params = []
        
    def startAction(self, action, params=[]):
        self.action = action
        self.params = params
        self.start()

    def run(self):
        try:
            #处理登录请求
            if self.action == 'login':
                if len(self.params) == 1:
                    localOnly = self.params[0]
                    mode = self.facade.prepare_network(localOnly = localOnly)
                else:
                    localOnly = self.params[0]
                    user = self.params[1]
                    pwd = self.params[2]
                    mode = self.facade.prepare_network(user=user, password=pwd, localOnly=localOnly)
                self.sinOutLogin.emit(mode)
            #处理导出请求    
            elif self.action == 'export':
                filename = self.params[0]
                self.facade.export2excel(filename)
                self.sinOutExport.emit()
            #处理启动服务器
            elif self.action == 'startweb':
                self.facade.start_server_async()
                count = 20
                while(count > 0):
                    time.sleep(1)
                    count = count - 1
                    if self.facade.connection.is_listening(self.facade.port):
                        break
                self.sinOutAppStart.emit()
            elif self.action == 'synchronize':
                self.facade.synchronizeDatabase()
                self.facade.msg('同步完成')
        except Exception, ex:
            self.facade.msg(ex)
            self.sinOutFail.emit('error');
        

if __name__ == '__main__':
    
    
    f = Facade()
    
    f.prepare_network(localOnly=False)
#    f.start_server_async()
#    
#    while(1):
#        time.sleep(1)
#        if f.connection.is_listening(f.port):
#            break
    
#    time.sleep(10)
#    f.synchronizeDatabase()
    f.export2excel(u'信息化系统列表.xls')
