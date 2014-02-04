# -*- coding: utf-8 -*-
import sys, os
import re, time, ConfigParser, facade
from encrypt import Code
#from login import *
from Ui_main import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from login import LoginDlg
#from facade import *
#from facadethread import *

from singleton import *

reload(sys)
sys.setdefaultencoding('utf-8')


class MainDlg(QDialog, Ui_Dialog):
    
    def __init__(self, parent=None):
        super(MainDlg, self).__init__()
        self.facade = facade.Facade()
        self.setupUi(self)
        

        #这种方法信号槽会被触发2次，见
        #http://hi.baidu.com/kxw102/item/cffc9e0ef1eadbcb75cd3c0c
        #self.btnEdit.released.connect(self.on_btnEdit_pressed)
        self.connect(self.btnEdit, QtCore.SIGNAL("released"), self.on_btnEdit_pressed)
        self.connect(self.btnExport, QtCore.SIGNAL("released"), self.on_btnExport_pressed)

                
        #构造后台逻辑线程
        self.facadeThread = facade.FacadeThread(self.facade)
        
        #注册facade的返回响应
        self.facadeThread.sinOutLogin.connect(self.onLogon)
        self.facadeThread.sinOutAppStart.connect(self.openBrowser)
        self.facadeThread.sinOutExport.connect(self.onExport)
        #初始化打印信号/槽
        self.facade.sinOutMsg.connect(self.onMsg)
        
        
        #绑定设置用户
        self.btnConfigUser.clicked.connect(self.showLoginDlg)
        
        
    #导出按钮按下
    def on_btnExport_pressed(self):
        filename = QtGui.QFileDialog.getSaveFileName(self, caption=u'选择保存路径', directory=u'信息化系统列表.xls', filter='*.xls')
        if filename <> '':
            self.facadeThread.startAction('export', [filename])
        else:
            self.facade.msg('取消导出')
    
    #成功导出
    def onExport(self):
        QtGui.QMessageBox.information(self, u'结果', u'导出成功')
        pass
    
    def on_btnEdit_pressed(self):
        #打开测试页面
        if self.facade.app is None:
            if not self.facadeThread.isRunning():
                self.facadeThread.startAction('startweb', [])
        else:
            self.openBrowser()

    def openBrowser(self):
        os.system('start http://localhost:' + str(self.facade.port))
            
    #响应登录成功事件        
    def onLogon(self, mode):
        #更新连接方面的信息
        if mode == 'remote':
            str_user = self.facade.logonUser + u'[登录成功]'
            str_mode = u'连接状态：[在线]'
        else: #local
            str_user = self.facade.logonUser + u'[登录失败]'
            str_mode = u'连接状态：[离线]'
        
        self.lblMode.setText(str_mode)
        self.lblUser.setText(str_user)
        
        
        #TODO：应该有N种状态：(匿名，非匿名)*(在线，离线)*(数据库可读,数据库不可写,不可用)
        
        #更新数据库方面的信息
        self.facade.msg('正在检查数据库完整性')
        dbRead, dbWrite, version = self.facade.checkDatabase(mode == 'local')
        
        if dbRead:
            #设置编辑属性
            self.lblVersion.setText(u'版本{0}，最后修改：{1}'.format(version['version'], version['modifytime']))
            self.btnEdit.setEnabled(True)
            self.btnExport.setEnabled(True)
            
            if  mode == 'remote':
                #远程连接时，还要看看是否可写
                if dbWrite:
                    str_editable = u'编辑状态：[可写]'
                else:
                    str_editable = u'编辑状态：[只读]'
                    
                #登录   成功后立刻同步
                self.facadeThread.startAction('synchronize', [])
            else: #local
                str_editable = u'编辑状态：[只读]'
            self.lblEditable.setText(str_editable)
        else:
            self.lblEditable.setText(u'编辑状态：[数据库不可用]')
            self.lblEditable.setStyleSheet("color: rgb(255, 0, 0);")
        pass

    #响应消息提示    
    def onMsg(self, msg):
        text = self.txtMsg.toPlainText()
        text = msg + "\r\n" + text
        self.txtMsg.setPlainText(text)
    
    #显示登录框
    def showLoginDlg(self):
        loginDlg = LoginDlg()
        from configer import Config 
        #加载已经保存的用户
        config = Config(self.facade)
        config.loadUserFromIni()
        param = config.param
        
        loginDlg.txtUser.setText(param['user'])
        loginDlg.txtPassword.setText(param['password'])
        
        loginDlg.setModal(True)
        loginConfirm = loginDlg.exec_()
        if loginConfirm:
            user = loginDlg.txtUser.text()
            print user
            password = loginDlg.txtPassword.text()
            bSave = loginDlg.cbxSave.isChecked()
            if bSave:
                config.saveUserToIni({'user':user, 'password':password})

            userText = user + u'[登录中]';
            self.lblUser.setText(userText)
            form.facadeThread.startAction('login', [False, user, password])
    
    #加载以保存的用户名和密码进行自动登录
    def autoLogin(self, localOnly=False):
        userText = u'[自动登录中]';
        self.lblUser.setText(userText)
        self.facadeThread.startAction('login', [localOnly])
        


if __name__ == "__main__":
    
    
    me = SingleInstance()
    
    app = QApplication(sys.argv)
    form = MainDlg()
    form.show()
    #自动登录
    #for debug
    form.autoLogin()
    
    app.exec_()    
    
    
