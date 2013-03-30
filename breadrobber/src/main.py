# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import re, time, ConfigParser
from login import *
from Ui_main import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from facade import *


class MainDlg(QDialog, Ui_Dialog):
    
    def __init__(self, parent=None):
        super(MainDlg, self).__init__()
        self.facade = Facade()
        self.setupUi(self)
        self.setFixedSize(250, 331)
        
        #构造后台逻辑线程
        self.facadeThread = FacadeThread(self.facade)
        self.facadeThread.sinOutLogin.connect(self.onLogon)
        
        #加载数据线程
        self.facadeThread2 = FacadeThread(self.facade)
        self.facadeThread2.sinOutProductList.connect(self.onProductLoad)
        self.facadeThread2.sinOutNotify.connect(self.onProductChecked)

        #初始化打印信号/槽
        self.facade.sinOutMsg.connect(self.onMsg)
        
        #自动更新按钮文本
        self.appTimer = QtCore.QTimer(self)
        self.appTimer.timeout.connect(self.updateNotifyButton)
        self.timerCount = 0
        
        #初始化任务栏图标
        self.init_trayicon()
        
        #设置标题栏样式
        self.setWindowFlags(Qt.Window)
#        self.setWindowState(Qt.WindowNoState)
        
        #绑定设置用户
        self.btnConfigUser.clicked.connect(self.showLoginDlg) 
        
    def init_trayicon(self):
        #设置一个iconComboBox
        self.iconComboBox = QtGui.QComboBox()
        self.iconComboBox.addItem(
            QtGui.QIcon('image/toast.png'), "Dmyz")
        #-------------------通知区域图标右键菜单start------------------
        self.restoreAction = QtGui.QAction(u"显示窗口", self,
                triggered=self.showNormal)
        self.quitAction = QtGui.QAction(u"退出", self,
                triggered=QtGui.qApp.quit)
        #弹出的菜单的行为，包括退出，还原，最小化
        self.trayIconMenu = QtGui.QMenu(self)
        self.trayIconMenu.addAction(self.restoreAction)
        self.trayIconMenu.addAction(self.quitAction)
        self.trayIcon = QtGui.QSystemTrayIcon(self)
        self.trayIcon.setContextMenu(self.trayIconMenu)
        #-------------------通知区域图标右键菜单end------------------
        #设置通知区域的ICON
        self.iconComboBox.currentIndexChanged.connect(self.setIcon)
 
        #通知区域icon显示
        self.iconComboBox.setCurrentIndex(1)
        self.trayIcon.activated.connect(self.iconActivated)
    
    def closeEvent(self, event):
        event.ignore()
        #强制退出
        sys.exit()
        
    
    def changeEvent(self, event):
    # 判断是否为最小化事件
        if event.type() == QtCore.QEvent.WindowStateChange and self.isMinimized():
            # 设置隐藏
            self.setVisible(False)
            # 设置窗口标记(取消在左下角显示)
            self.setWindowFlags(QtCore.Qt.Tool)
            self.trayIcon.show()
    
    def __icon_activated(self, reason):
      if reason == QtGui.QSystemTrayIcon.DoubleClick:
        self.trayIcon.hide()
        self.show()

 
    def iconActivated(self, reason):
        if reason in (QtGui.QSystemTrayIcon.Trigger,
                      QtGui.QSystemTrayIcon.DoubleClick):
            self.trayIcon.hide()
            if self.windowType() == QtCore.Qt.Tool:
                # 设置窗口标记(包含最大化、最小化按钮)
                self.setWindowFlags(QtCore.Qt.Window)
            self.showNormal()
            self.activateWindow()
        elif reason == QtGui.QSystemTrayIcon.MiddleClick:
            self.showMessage()
 
    def setIcon(self, index):
        icon = self.iconComboBox.itemIcon(0)
        self.trayIcon.setIcon(icon)
        self.setWindowIcon(icon)
        self.trayIcon.setToolTip(self.iconComboBox.itemText(index))
 
    def showMessage(self, msg):
        #这里是可以设置弹出对话气泡的icon的，作为实验就省略了
        icon = QtGui.QSystemTrayIcon.MessageIcon()
        self.trayIcon.showMessage(u'提示', msg, icon, 1000)
 
    def getTasksNum(self):
        self.showMessage()
 

    def on_btnNotifyMission_pressed(self):
        curIndex = self.cmbProduct.currentIndex()
        productId = self.cmbProduct.itemData(curIndex).toString()
        productName = self.cmbProduct.currentText()
        if not self.facadeThread2.isRunning():
            self.facadeThread2.startAction('NotifyMission', [productId, productName])
            self.cmbProduct.setEnabled(False)
            
            #启动计时器
            self.timerCount = 0
            self.appTimer.start(1000)
            
        else:
            self.facadeThread2.terminate()
            self.onProductChecked(True)
        
    def onProductChecked(self, manual=False):
        self.cmbProduct.setEnabled(True)
        self.btnNotifyMission.setText(u'有货通知我');
        self.appTimer.stop()
        
        if not manual:
            if self.isMinimized():
                self.showMessage(u'你要的货已经有了')
            else:
                QtGui.QMessageBox.information(self, u'提示', u'你要的货已经有了')
        
    def onLogon(self, username, loginResult):
        #update 
        if loginResult:
            userText = username + u'[已登录]';
            self.lblUser.setText(userText)
            self.facadeThread2.startAction('ProductList')
            self.facade.msg(u'正在加载商品数据')
        else:
            userText = username + u'[未登录]';
            self.lblUser.setText(userText)
    
    def onProductLoad(self, productList):
        for p in productList:
            self.cmbProduct.addItem(unicode(p['name']), p['id'])
        self.gbxStep2.setEnabled(True)
    
    def onMsg(self, msg):
        text = self.txtMsg.toPlainText()
        text = msg + "\r\n" + text
        self.txtMsg.setPlainText(text)
    
    def updateNotifyButton(self):
        title = u'   有货通知我{0}{1}'.format('.' * self.timerCount, ' ' * (3 - self.timerCount))
        self.btnNotifyMission.setText(title)
        self.timerCount = (self.timerCount + 1) % 4 
    
    #显示登录框
    def showLoginDlg(self):
        loginDlg = LoginDlg()
        
        #加载已经保存的用户
        param = self.loadFromIni()
        loginDlg.txtUser.setText(param['user'])
        loginDlg.txtPassword.setText(param['password'])
        
        loginDlg.setModal(True)
        loginConfirm = loginDlg.exec_()
        if loginConfirm:
            user = loginDlg.txtUser.text()
            password = loginDlg.txtPassword.text()
            bSave = loginDlg.cbxSave.isChecked()
            if bSave:
                self.saveToIni({'user':user, 'password':password})
                
            form.facadeThread.startAction('Login', [user, password])
    
    def autoLogin(self):
        config = self.loadFromIni()
        user = config['user']
        if user == '':
            self.showLoginDlg()
        else:
            self.facadeThread.startAction('Login', [config['user'], config['password']])

    def loadFromIni(self):
        try:
            config = ConfigParser.ConfigParser()
            config.readfp(open('config.ini'))
            user = config.get("UserInfo", "user")
            password = config.get("UserInfo", "password")
            return {'user':user, 'password':password}
        except:
            return {'user':'', 'password':''}

    def saveToIni(self, param):
        try:
            config = ConfigParser.ConfigParser()
    
            # set a number of parameters
            config.add_section("UserInfo")
            config.set("UserInfo", "user", param['user'])
            config.set("UserInfo", "password", param['password'])
    
            config.write(open('config.ini', "w"))
        except Exception, ex:
            self.facade.msg(ex)
            
class FacadeThread(QThread):
     
    sinOutLogin = pyqtSignal(str, bool)
    sinOutProductList = pyqtSignal(list)
    sinOutNotify = pyqtSignal()
    
    def __init__(self, facade, parent=None):
        super(FacadeThread, self).__init__(parent)
        self.facade = facade
        self.action = 'Login'
        self.params = []
    
    def startAction(self, action, params=[]):
        self.action = action
        self.params = params
        self.start()
        
    def run(self):
        if self.action == 'Login':
            loginResult = self.facade.performLogin(self.params[0], self.params[1])
            self.sinOutLogin.emit(self.params[0], loginResult)
        elif self.action == 'ProductList':
            productList = self.facade.getProductList()
            self.sinOutProductList.emit(productList)
        elif self.action == 'NotifyMission':
            while True:
                hasVault = self.facade.checkProductVault(self.params[0])
                if hasVault:
                    msgText = self.params[0] + " " + self.params[1] + u" 有货"
                else:
                    msgText = self.params[0] + " " + self.params[1] + u" 无货"
                self.facade.msg(msgText)
                
                if hasVault:
                    break
                time.sleep(30)
            
            self.sinOutNotify.emit()
    
    

if __name__ == "__main__":
    import sys
    
    app = QApplication(sys.argv)
    
    form = MainDlg()
    form.show()
    #自动登录
    form.autoLogin()
    
    app.exec_()
    
    
    
