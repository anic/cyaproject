# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Program\python\breadrobber\src\main.ui'
#
# Created: Tue Apr 02 00:28:51 2013
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
        Dialog.resize(253, 527)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("image/toast.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout_2 = QtGui.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
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
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.gbxStep2 = QtGui.QGroupBox(Dialog)
        self.gbxStep2.setEnabled(False)
        self.gbxStep2.setCheckable(False)
        self.gbxStep2.setChecked(False)
        self.gbxStep2.setObjectName(_fromUtf8("gbxStep2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.gbxStep2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_2 = QtGui.QLabel(self.gbxStep2)
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.cmbProduct = QtGui.QComboBox(self.gbxStep2)
        self.cmbProduct.setMinimumSize(QtCore.QSize(150, 0))
        self.cmbProduct.setObjectName(_fromUtf8("cmbProduct"))
        self.gridLayout_3.addWidget(self.cmbProduct, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.scrollArea = QtGui.QScrollArea(self.gbxStep2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 280))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.taskContent = QtGui.QWidget()
        self.taskContent.setGeometry(QtCore.QRect(0, 0, 209, 276))
        self.taskContent.setObjectName(_fromUtf8("taskContent"))
        self.scrollArea.setWidget(self.taskContent)
        self.verticalLayout.addWidget(self.scrollArea)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.cbxCheckAll = QtGui.QCheckBox(self.gbxStep2)
        self.cbxCheckAll.setObjectName(_fromUtf8("cbxCheckAll"))
        self.gridLayout_4.addWidget(self.cbxCheckAll, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(37, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 0, 1, 1, 1)
        self.cbxContinue = QtGui.QCheckBox(self.gbxStep2)
        self.cbxContinue.setChecked(True)
        self.cbxContinue.setObjectName(_fromUtf8("cbxContinue"))
        self.gridLayout_4.addWidget(self.cbxContinue, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_4)
        self.btnNotifyMission = QtGui.QPushButton(self.gbxStep2)
        self.btnNotifyMission.setObjectName(_fromUtf8("btnNotifyMission"))
        self.verticalLayout.addWidget(self.btnNotifyMission)
        self.gridLayout_2.addWidget(self.gbxStep2, 1, 0, 1, 1)
        self.txtMsg = QtGui.QPlainTextEdit(Dialog)
        self.txtMsg.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.txtMsg.setFont(font)
        self.txtMsg.setUndoRedoEnabled(False)
        self.txtMsg.setReadOnly(True)
        self.txtMsg.setPlainText(_fromUtf8(""))
        self.txtMsg.setObjectName(_fromUtf8("txtMsg"))
        self.gridLayout_2.addWidget(self.txtMsg, 2, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "抢包子助手", None))
        self.groupBox.setTitle(_translate("Dialog", "登录", None))
        self.lblUser.setText(_translate("Dialog", "请设定用户", None))
        self.btnConfigUser.setText(_translate("Dialog", "...", None))
        self.gbxStep2.setTitle(_translate("Dialog", "商品", None))
        self.label_2.setText(_translate("Dialog", "商品分类", None))
        self.cbxCheckAll.setText(_translate("Dialog", "全选/反选", None))
        self.cbxContinue.setText(_translate("Dialog", "有货继续扫描", None))
        self.btnNotifyMission.setText(_translate("Dialog", "有货通知我", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

