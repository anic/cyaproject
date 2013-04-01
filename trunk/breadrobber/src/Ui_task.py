# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Program\python\breadrobber\src\task.ui'
#
# Created: Mon Apr 01 23:34:52 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(267, 493)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.scrollArea = QtGui.QScrollArea(Dialog)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.taskContent = QtGui.QWidget()
        self.taskContent.setGeometry(QtCore.QRect(0, 0, 229, 396))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.taskContent.sizePolicy().hasHeightForWidth())
        self.taskContent.setSizePolicy(sizePolicy)
        self.taskContent.setAutoFillBackground(True)
        self.taskContent.setObjectName(_fromUtf8("taskContent"))
        self.scrollArea.setWidget(self.taskContent)
        self.verticalLayout.addWidget(self.scrollArea)
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cbxCheckAll = QtGui.QCheckBox(self.frame)
        self.cbxCheckAll.setObjectName(_fromUtf8("cbxCheckAll"))
        self.horizontalLayout.addWidget(self.cbxCheckAll)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtGui.QLabel(self.frame)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addWidget(self.frame)
        self.btnStartTask = QtGui.QPushButton(Dialog)
        self.btnStartTask.setObjectName(_fromUtf8("btnStartTask"))
        self.verticalLayout.addWidget(self.btnStartTask)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "多目标", None))
        self.cbxCheckAll.setText(_translate("Dialog", "全选/反选", None))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><a href=\"http://ygjy.gz.gmcc.net/gzxz/ebusiness/admin/vmerchandist!executeSearch.action\"><span style=\" text-decoration: underline; color:#0000ff;\">商品列表</span></a></p></body></html>", None))
        self.btnStartTask.setText(_translate("Dialog", "开始", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

