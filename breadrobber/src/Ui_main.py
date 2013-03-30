# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Program\python\breadrobber\src\main.ui'
#
# Created: Sat Mar 30 16:15:47 2013
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
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(250, 331)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("image/toast.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(9, 9, 233, 51))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.layoutWidget = QtGui.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 20, 211, 22))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lblUser = QtGui.QLabel(self.layoutWidget)
        self.lblUser.setObjectName(_fromUtf8("lblUser"))
        self.horizontalLayout.addWidget(self.lblUser)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnConfigUser = QtGui.QToolButton(self.layoutWidget)
        self.btnConfigUser.setObjectName(_fromUtf8("btnConfigUser"))
        self.horizontalLayout.addWidget(self.btnConfigUser)
        self.gbxStep2 = QtGui.QGroupBox(Dialog)
        self.gbxStep2.setEnabled(False)
        self.gbxStep2.setGeometry(QtCore.QRect(10, 70, 233, 101))
        self.gbxStep2.setCheckable(False)
        self.gbxStep2.setChecked(False)
        self.gbxStep2.setObjectName(_fromUtf8("gbxStep2"))
        self.layoutWidget1 = QtGui.QWidget(self.gbxStep2)
        self.layoutWidget1.setGeometry(QtCore.QRect(11, 21, 211, 22))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.formLayout = QtGui.QFormLayout(self.layoutWidget1)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_2 = QtGui.QLabel(self.layoutWidget1)
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.cmbProduct = QtGui.QComboBox(self.layoutWidget1)
        self.cmbProduct.setObjectName(_fromUtf8("cmbProduct"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.cmbProduct)
        self.btnNotifyMission = QtGui.QPushButton(self.gbxStep2)
        self.btnNotifyMission.setGeometry(QtCore.QRect(10, 60, 211, 31))
        self.btnNotifyMission.setObjectName(_fromUtf8("btnNotifyMission"))
        self.txtMsg = QtGui.QPlainTextEdit(Dialog)
        self.txtMsg.setGeometry(QtCore.QRect(10, 180, 231, 141))
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
        Dialog.setWindowTitle(_translate("Dialog", "抢包子", None))
        self.groupBox.setTitle(_translate("Dialog", "步骤1：登录", None))
        self.lblUser.setText(_translate("Dialog", "请设定用户", None))
        self.btnConfigUser.setText(_translate("Dialog", "...", None))
        self.gbxStep2.setTitle(_translate("Dialog", "步骤2：选择商品", None))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><a href=\"http://ygjy.gz.gmcc.net/gzxz/ebusiness/admin/vmerchandist!executeSearch.action\"><span style=\" text-decoration: underline; color:#0000ff;\">商品</span></a></p></body></html>", None))
        self.btnNotifyMission.setText(_translate("Dialog", "有货通知我", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

