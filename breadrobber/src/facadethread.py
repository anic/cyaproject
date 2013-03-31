# -*- coding: utf-8 -*-
import time
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class FacadeThread(QThread):
     
    sinOutLogin = pyqtSignal(str, bool)
    sinOutProductList = pyqtSignal(list)
    sinOutNotifyOne = pyqtSignal()
    sinOutNotifyMany = pyqtSignal(str, bool)
    sinOutNotifyFinish = pyqtSignal()
    
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
        elif self.action == 'NotifyOne':
            while True:
                inStock = self.facade.checkProductVault(self.params[0])
                if inStock:
                    msgText = self.params[0] + " " + self.params[1] + u" 有货"
                else:
                    msgText = self.params[0] + " " + self.params[1] + u" 缺货"
                self.facade.msg(msgText)
                
                if inStock:
                    break
                
                #每30秒刷新一次
                time.sleep(30)
            
            self.sinOutNotifyOne.emit()
        elif self.action == 'NotifyMany':
            ids = self.params[0]
            names = self.params[1]
            bGlobal = True
            while bGlobal:
                for i in range(0, len(ids)):
                    inStock = self.facade.checkProductVault(ids[i])
                    if inStock:
                        msgText = ids[i] + " " + names[i] + u" 有货"
                    else:
                        msgText = ids[i] + " " + names[i] + u" 缺货"
                    self.facade.msg(msgText)
                    self.sinOutNotifyMany.emit(ids[i], inStock)
                    
                    #完成这一轮的扫描                    
                    if inStock and bGlobal:
                        bGlobal = False
                    
                    #每10秒刷新一次
                    time.sleep(1)
            
            self.sinOutNotifyFinish.emit()
