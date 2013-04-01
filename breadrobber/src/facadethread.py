# -*- coding: utf-8 -*-
import time
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class FacadeThread(QThread):
     
    sinOutLogin = pyqtSignal(str, bool)
    sinOutProductList = pyqtSignal(list)
    sinOutNotifyOne = pyqtSignal()
    sinOutNotifyMany = pyqtSignal(str, int)
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
                if inStock == 0:
                    msgText = u'{0} {1} 缺货'.format(self.params[0], self.params[1])
                else:
                    msgText = u'{0} {1} 有货[{2}]'.format(self.params[0], self.params[1], inStock)
                self.facade.msg(msgText)
                
                if inStock > 0:
                    break
                
                #每30秒刷新一次
                time.sleep(30)
            
            self.sinOutNotifyOne.emit()
        elif self.action == 'NotifyMany':
            ids = self.params[0]
            names = self.params[1]
            bGlobal = True
            bFirstRound = True
            while bGlobal:
                for i in range(0, len(ids)):
                    inStock = self.facade.checkProductVault(ids[i])
                    if inStock == 0:
                        msgText = u'{0} {1} 缺货'.format(ids[i], names[i])
                    else:
                        msgText = u'{0} {1} 有货[{2}]'.format(ids[i], names[i], inStock)
                        
                    self.facade.msg(msgText)
                    self.sinOutNotifyMany.emit(ids[i], inStock)
                    
                    #完成这一轮的扫描                    
#                    if inStock and bGlobal:
#                        bGlobal = False
                    
                    #第一圈停留时间短一些
                    if not bFirstRound:
                        time.sleep(30)
            
                bFirstRound = False
            self.sinOutNotifyFinish.emit()
