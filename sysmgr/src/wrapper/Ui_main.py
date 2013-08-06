# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Program\python\sysmgr\src\wrapper\main.ui'
#
# Created: Tue Aug 06 22:17:53 2013
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
        Dialog.resize(275, 456)
        self.btnUpdate = QtGui.QPushButton(Dialog)
        self.btnUpdate.setGeometry(QtCore.QRect(20, 30, 91, 51))
        self.btnUpdate.setObjectName(_fromUtf8("btnUpdate"))
        self.btnStartWeb = QtGui.QPushButton(Dialog)
        self.btnStartWeb.setGeometry(QtCore.QRect(160, 30, 91, 51))
        self.btnStartWeb.setObjectName(_fromUtf8("btnStartWeb"))
        self.txtMsg = QtGui.QPlainTextEdit(Dialog)
        self.txtMsg.setGeometry(QtCore.QRect(20, 110, 241, 241))
        self.txtMsg.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.txtMsg.setFont(font)
        self.txtMsg.setUndoRedoEnabled(False)
        self.txtMsg.setReadOnly(True)
        self.txtMsg.setPlainText(_fromUtf8(""))
        self.txtMsg.setObjectName(_fromUtf8("txtMsg"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "系统信息维护助手", None))
        self.btnUpdate.setText(_translate("Dialog", "导出Excel", None))
        self.btnStartWeb.setText(_translate("Dialog", "维护信息", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

