# -*- coding: utf-8 -*-

import re, time, ConfigParser
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Ui_task import *
from facade import Facade
from facadethread import FacadeThread

class TaskDlg(QDialog, Ui_Dialog):
    
    def __init__(self, parent=None):
        super(TaskDlg, self).__init__()
        self.facade = Facade()
        self.setupUi(self)
        self.facade = Facade()
        self.thread = FacadeThread(self.facade)
        self.thread.sinOutProductList.connect(self.onProductLoad)
        self.thread.sinOutNotifyMany.connect(self.onProductChecked)
        self.thread.sinOutNotifyFinish.connect(self.resetControl)
        self.controls = []
        self.controlMap = {}
        self.isNotified = True
        
        
        
    def on_cbxCheckAll_released(self):
        val = self.cbxCheckAll.isChecked()
        for c in self.controls:
            c.setChecked(val)
        
    def on_btnStartTask_pressed(self):
        if self.thread.isRunning():
            self.thread.terminate()
            self.resetControl()
            self.btnStartTask.setText(u'开始')
            return
        
        
        
        
            
        for c in self.controls:
            c.setEnabled(not c.isEnabled())

        targetIds = []
        targetNames = []            
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
        
        self.isNotified = False
        self.btnStartTask.setText(u'停止')
        self.thread.startAction('NotifyMany', [targetIds, targetNames])
    
    def onProductLoad(self, products):
        for i in range(0, len(products)):
            checkBox = QtGui.QCheckBox(ui.taskContent)
            checkBox.setGeometry(QtCore.QRect(10, 10 + 20 * i, 250, 17))
            checkBox.setText(unicode(products[i]['name']))
            checkBox.setObjectName(u'cbx{0}'.format(products[i]['id']))
            self.controls.append(checkBox)
        
        self.show()
        
    #根据商品编号查找控件
    def findItemControl(self, id):
        for c in self.controls:
            cid = str(c.objectName())[3:] #prefix is 'cbx'
            if cid == id:
                return c
        
        return None
    
    def resetControl(self):
        for c in self.controls:
            c.setEnabled(not c.isEnabled())
        self.onProductChecked('', False)
    
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
            QtGui.QMessageBox.information(self, u'提示', u'你要的货已经有了')
    
if __name__ == '__main__':
    
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = TaskDlg()
    
#    products = [{'id':"M000162000001", 'name':"喜尔宾测试"},
#    {'id':"M000139000050", 'name':"绿色菜篮农家初生蛋（30枚）"},
#    {'id':"M000139000051", 'name':"绿色菜篮农家土鸡蛋（30枚）"},
#    {'id':"M000127000015", 'name':"（金海）御品核桃酥"},
#    {'id':"M000127000017", 'name':"(金海)燕麦小馒头"},
#    {'id':"M000001000629", 'name':"（金海）北方小馒头"},
#    {'id':"M000127000020", 'name':"（金海）吐司大面包"},
#    {'id':"M000001000631", 'name':"（金海）燕麦大馒头"},
#    {'id':"M000146000018", 'name':"年货测试"},
#    {'id':"M000001000622", 'name':"（金海）蜜汁焗餐包"},
#    {'id':"M000127000022", 'name':"（金海）牛角包"},
#    {'id':"M000127000005", 'name':"（金海）酥皮包"},
#    {'id':"M000001000625", 'name':"（金海）古法鸡蛋糕"},
#    {'id':"M000127000023", 'name':"（金海）糯米鸡"},
#    {'id':"M000001000627", 'name':"（金海）清香靓花卷"},
#    {'id':"M000001000628", 'name':"（金海）新鲜生肉包"},
#    {'id':"M000127000011", 'name':"（金海）东北大馒头"},
#    {'id':"M000127000025", 'name':"(金海)风味川西饼"}]
#    ui.onProductLoad(products)
    
#    ui.show()
    ui.facade.performLogin('chengyaoan', 'cya!@#45')
    ui.thread.startAction('ProductList')
    sys.exit(app.exec_())
