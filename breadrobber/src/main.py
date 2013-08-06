# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import re, time, ConfigParser
from encrypt import Code
from login import *
from Ui_main import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from facade import *
from facadethread import *

class MainDlg(QDialog, Ui_Dialog):
    
    product_types = [{'name':u'全部 ', 'id':''},
                   {'name':u'点心坊 ', 'id':'11'},
                   {'name':u'手工面类 ', 'id':'12'},
                   {'name':u'净菜类 ', 'id':'10'},
                   {'name':u'鲜肉档 ', 'id':'13'}
                   ]
    
    
    def __init__(self, parent=None):
        super(MainDlg, self).__init__()
        self.facade = Facade()
        self.setupUi(self)
        
        #构造后台逻辑线程
        self.facadeThread = FacadeThread(self.facade)
        self.facadeThread.sinOutLogin.connect(self.onLogon)
        
        #加载数据线程
        self.facadeThread2 = FacadeThread(self.facade)
        self.facadeThread2.sinOutProductList.connect(self.onProductLoad)
        self.facadeThread2.sinOutNotifyMany.connect(self.onProductChecked)
        self.facadeThread2.sinOutNotifyFinish.connect(self.finishMission)
        

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
        
        #绑定设置用户
        self.btnConfigUser.clicked.connect(self.showLoginDlg) 
        
        #记录增加的checkbox控件
        self.controls = []
        self.isNotified = True
        
        #记录是否准备好分类信息
        self.bTypeReady = False
        
        self.cmbProduct.currentIndexChanged.connect(self.onTypeChanged)
        
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
    
    #修改关闭时的函数，为了可以最小化到托盘
    def closeEvent(self, event):
        event.ignore()
        #强制退出
        sys.exit()
        
    #修改关闭时的函数，为了可以最小化到托盘
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
 
    #显示气泡信息
    def showMessage(self, msg):
        #这里是可以设置弹出对话气泡的icon的，作为实验就省略了
        icon = QtGui.QSystemTrayIcon.MessageIcon()
        self.trayIcon.showMessage(u'提示', msg, icon, 1000)
 
    def onTypeChanged(self):
        if not self.bTypeReady:
            return
        #好像变化前和变化后会重复
        index = self.cmbProduct.currentIndex()
        sortId = self.cmbProduct.itemData(index).toString()
            
        self.facadeThread2.startAction('ProductList', [sortId])
        self.facade.msg(u'正在加载商品数据[{0}]'.format(sortId))
    
    def on_btnNotifyMission_pressed(self):
            
        if self.facadeThread2.isRunning():
            self.facadeThread2.terminate()
            
            self.finishMission()
            
            return

        targetIds = []
        targetNames = []            
        bContinue = self.cbxContinue.isChecked()
        for c in self.controls:
            if c.isChecked():
                targetIds.append(str(c.objectName())[3:]) #prefix is 'cbx'
                #去掉文本中的[有货]
                text = unicode(str(c.text()))
                index = text.find('[')
                if index != -1:
                    text = text[:index]
                targetNames.append(text)
        
        if len(targetIds) == 0:
           QtGui.QMessageBox.warning(self, u'警告', u'至少选择一类商品')
           return
        
        #确定可以开始执行
        for c in self.controls:
           c.setEnabled(False)
           
        self.cbxCheckAll.setEnabled(False)
        self.cmbProduct.setEnabled(False)
        
        self.isNotified = False
        self.btnNotifyMission.setText(u'运行中')
        self.facadeThread2.startAction('NotifyMany', [targetIds, targetNames, bContinue])
        
        #启动计时器
        self.timerCount = 0
        self.appTimer.start(1000)
        
        
    def onLogon(self, username, loginResult):
        #update 
        if loginResult:
            userText = username + u'[已登录]';
            self.lblUser.setText(userText)
            
            #添加静态的分类信息
            self.onProductTypeLoad(self.product_types)
            #设置默认为点心坊,1
            self.bTypeReady = True
            self.cmbProduct.setCurrentIndex(1)
#            sortId = self.cmbProduct.itemData(1).toString()
#            self.facadeThread2.startAction('ProductList', [sortId])
#            self.facade.msg(u'正在加载商品数据')
        else:
            userText = username + u'[登录失败]';
            self.lblUser.setText(userText)
    
    def onProductTypeLoad(self, types):
        for p in types:
            self.cmbProduct.addItem(unicode(p['name']), p['id'])
        
        self.gbxStep2.setEnabled(True)
    
    def onProductLoad(self, products):
        #清空controls
        for c in self.controls:
            c.hide()
            c.destroy()
        
        #清空controls
        del self.controls[:]
        
        #初始化全选按钮
        self.cbxCheckAll.setChecked(False)
        
        for i in range(0, len(products)):
            checkBox = QtGui.QCheckBox(self.taskContent)
            checkBox.setGeometry(QtCore.QRect(10, 10 + 20 * i, 250, 20))
            checkBox.setText(unicode(products[i]['name']))
            checkBox.setObjectName(u'cbx{0}'.format(products[i]['id']))
            checkBox.show()
            self.controls.append(checkBox)
        
        #计算最小高度
        self.taskContent.setMinimumHeight(10 + 20 * len(products) + 20)
        
    #全选和反选的功能
    def on_cbxCheckAll_released(self):
        val = self.cbxCheckAll.isChecked()
        for c in self.controls:
            c.setChecked(val)
    
    def onMsg(self, msg):
        text = self.txtMsg.toPlainText()
        text = msg + "\r\n" + text
        self.txtMsg.setPlainText(text)
    
    def updateNotifyButton(self):
        title = u'   运行中{0}{1}'.format('.' * self.timerCount, ' ' * (3 - self.timerCount))
        self.btnNotifyMission.setText(title)
        self.timerCount = (self.timerCount + 1) % 4
        
        #发现运行已经停止
        if not self.facadeThread2.isRunning():
            self.facadeThread2.start()
         
    
    def finishMission(self):
        self.appTimer.stop()
        self.btnNotifyMission.setText(u'有货通知我')
        
        for c in self.controls:
            c.setEnabled(True)
    
        self.cbxCheckAll.setEnabled(True)
        self.cmbProduct.setEnabled(True)
        
        
    def onProductChecked(self, id, instock):
        
        for c in self.controls:
            if c.isChecked():
                text = c.text()
                text = unicode(str(text)) #QString转换为str
                index = text.find('<')
                if index != -1:
                    text = text[0:index]
                c.setText(text)
        
        #找到目标控件
        cbx = self.findItemControl(id)
        if cbx != None:
            text = cbx.text()
            text = unicode(str(text)) #QString转换为str
            index = text.find('[')
            if index != -1:
                text = text[0:index]
            
            if instock > 0:
                cbx.setStyleSheet("color: rgb(0, 85, 0);")
                cbx.setText(text + u'[有货,{0}]<<'.format(instock))
                
            else:
                cbx.setStyleSheet("color: rgb(85, 0, 0);") 
                cbx.setText(text + u'[缺货]<<')
        
        if instock and not self.isNotified:
            self.isNotified = True
            if self.isMinimized():
                self.showMessage(u'你要的货已经有了')
            else:
                QtGui.QMessageBox.information(self, u'提示', u'你要的货已经有了')
    
    
    
    #根据商品编号查找控件
    def findItemControl(self, id):
        for c in self.controls:
            cid = str(c.objectName())[3:] #prefix is 'cbx'
            if cid == id:
                return c
        
        return None
    
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

            userText = user + u'[登录中]';
            self.lblUser.setText(userText)
            form.facadeThread.startAction('Login', [user, password])
    
    #加载以保存的用户名和密码进行自动登录
    def autoLogin(self):
        config = self.loadFromIni()
        user = config['user']
        if user == '':
            self.showLoginDlg()
        else:
            userText = config['user'] + u'[登录中]';
            self.lblUser.setText(userText)
            self.facadeThread.startAction('Login', [config['user'], config['password']])

    #保存到配置文件ini
    def loadFromIni(self):
        try:
            config = ConfigParser.ConfigParser()
            config.readfp(open('config.ini'))
            user = config.get("UserInfo", "user")
            password = config.get("UserInfo", "password")
            
            if user != '':
                code = Code(user)
                password = code.decode(password)
                #如果解析错了，则重置为空
                if password is None:
                    password = ''
            
            return {'user':user, 'password':password}
        except:
            return {'user':'', 'password':''}

    def saveToIni(self, param):
        try:
            
            if param['user'] != '':
                code = Code(unicode(param['user']))
                encrypted = code.encode(unicode(param['password']))
            else:
                encrypted = param['password']
            
            
            config = ConfigParser.ConfigParser()
            
            # set a number of parameters
            config.add_section("UserInfo")
            config.set("UserInfo", "user", param['user'])
            config.set("UserInfo", "password", encrypted)
    
            config.write(open('config.ini', "w"))
        except Exception, ex:
            self.facade.msg(ex)
            

    
    


if __name__ == "__main__":
    
    from singleton import *
    me = SingleInstance()
    
    import sys
    app = QApplication(sys.argv)
    form = MainDlg()
    form.show()
    #自动登录
    form.autoLogin()
    
    app.exec_()    
    
    
