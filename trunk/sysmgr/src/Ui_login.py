# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Program\python\sysmgr\src\login.ui'
#
# Created: Fri Feb 07 20:40:15 2014
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
        Dialog.resize(197, 135)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("image/toast.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setModal(True)
        self.txtPassword = QtGui.QLineEdit(Dialog)
        self.txtPassword.setGeometry(QtCore.QRect(60, 50, 121, 20))
        self.txtPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.txtPassword.setObjectName(_fromUtf8("txtPassword"))
        self.txtUser = QtGui.QLineEdit(Dialog)
        self.txtUser.setGeometry(QtCore.QRect(60, 20, 121, 20))
        self.txtUser.setObjectName(_fromUtf8("txtUser"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 36, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 24, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(20, 100, 156, 23))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.cbxSave = QtGui.QCheckBox(Dialog)
        self.cbxSave.setGeometry(QtCore.QRect(60, 77, 131, 17))
        self.cbxSave.setObjectName(_fromUtf8("cbxSave"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.txtUser, self.txtPassword)
        Dialog.setTabOrder(self.txtPassword, self.cbxSave)
        Dialog.setTabOrder(self.cbxSave, self.buttonBox)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "登录信息", None))
        self.txtPassword.setPlaceholderText(_translate("Dialog", "Portal密码", None))
        self.txtUser.setPlaceholderText(_translate("Dialog", "Portal账号", None))
        self.label.setText(_translate("Dialog", "用户名", None))
        self.label_2.setText(_translate("Dialog", "密码", None))
        self.cbxSave.setText(_translate("Dialog", "本地保存用户名密码", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

