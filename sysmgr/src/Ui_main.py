# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Program\python\sysmgr\src\main.ui'
#
# Created: Fri Jan 31 19:03:00 2014
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
        Dialog.resize(272, 513)
        self.gridLayout_2 = QtGui.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.btnEdit = QtGui.QPushButton(self.groupBox_2)
        self.btnEdit.setEnabled(False)
        self.btnEdit.setCheckable(False)
        self.btnEdit.setAutoDefault(False)
        self.btnEdit.setFlat(False)
        self.btnEdit.setObjectName(_fromUtf8("btnEdit"))
        self.verticalLayout.addWidget(self.btnEdit)
        self.btnExport = QtGui.QPushButton(self.groupBox_2)
        self.btnExport.setEnabled(False)
        self.btnExport.setObjectName(_fromUtf8("btnExport"))
        self.verticalLayout.addWidget(self.btnExport)
        self.gridLayout_2.addWidget(self.groupBox_2, 4, 0, 1, 1)
        self.txtMsg = QtGui.QPlainTextEdit(Dialog)
        self.txtMsg.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.txtMsg.setFont(font)
        self.txtMsg.setUndoRedoEnabled(False)
        self.txtMsg.setReadOnly(True)
        self.txtMsg.setPlainText(_fromUtf8(""))
        self.txtMsg.setObjectName(_fromUtf8("txtMsg"))
        self.gridLayout_2.addWidget(self.txtMsg, 5, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lblEditable = QtGui.QLabel(self.groupBox)
        self.lblEditable.setObjectName(_fromUtf8("lblEditable"))
        self.gridLayout.addWidget(self.lblEditable, 2, 0, 1, 1)
        self.lblMode = QtGui.QLabel(self.groupBox)
        self.lblMode.setObjectName(_fromUtf8("lblMode"))
        self.gridLayout.addWidget(self.lblMode, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lblUser = QtGui.QLabel(self.groupBox)
        self.lblUser.setObjectName(_fromUtf8("lblUser"))
        self.horizontalLayout.addWidget(self.lblUser)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnConfigUser = QtGui.QToolButton(self.groupBox)
        self.btnConfigUser.setObjectName(_fromUtf8("btnConfigUser"))
        self.horizontalLayout.addWidget(self.btnConfigUser)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.lblVersion = QtGui.QLabel(self.groupBox)
        self.lblVersion.setText(_fromUtf8(""))
        self.lblVersion.setObjectName(_fromUtf8("lblVersion"))
        self.gridLayout.addWidget(self.lblVersion, 3, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 2, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "系统信息维护助手", None))
        self.groupBox_2.setTitle(_translate("Dialog", "动作", None))
        self.btnEdit.setText(_translate("Dialog", "维护系统信息[网页]", None))
        self.btnExport.setText(_translate("Dialog", "导出系统信息[Excel]", None))
        self.groupBox.setTitle(_translate("Dialog", "登录", None))
        self.lblEditable.setText(_translate("Dialog", "编辑状态", None))
        self.lblMode.setText(_translate("Dialog", "连接状态", None))
        self.lblUser.setText(_translate("Dialog", "请设定用户", None))
        self.btnConfigUser.setText(_translate("Dialog", "设置", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

