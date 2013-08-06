# -*- coding: utf-8 -*-
import connector, configer, dao, sysmain, datetime, thread,time
from PyQt4.QtGui import *
from PyQt4.QtCore import *


class Facade:
    
    sinOutMsg = pyqtSignal(str)

    port = 8080
    remote = None
    database = None
    app = None
        
    def prepare_network(self):
        self.connection = connector.fsconnection()
        cf = configer.instance().param
    
        #在内网环境
#    if conn.check_netuse(cf['remotepath'], 'GZIAP\\' + cf['username'], cf['password']):
#        print u'无法连接目标'
#        mydatabase = cf['remotepath'] + "\\" + cf['location'].decode('gbk').encode('utf-8')
#    else:
#        mydatabase = cf['localpath']
        self.database = cf['localpath']
        self.port = self.connection.check_port()
        
        dao._DATABASE = self.database
        pass
    
    def start_server(self):
        #使用多线程启动服务器
        thread.start_new_thread(self.thread_startserver, (1, 1))  
        pass
    
    def thread_startserver(self, no, interval):
        self.app = sysmain.sysmgrapp(sysmain.urls, globals())
        self.app.run(port=self.port)
        pass
        
    def __init__(self):
        pass
    
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
            self.sinOutMsg.emit(strMsg)
        except:
            pass
    

if __name__ == '__main__':
    f = Facade()
    f.prepare_network()
    f.start_server()
    print 'server starting'
    while(1):
        time.sleep(1)
        if f.connection.is_listening(f.port):
            break
    
    print 'server started'
    print 'close in 10s'
    time.sleep(10)
