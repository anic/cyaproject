# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Program\python\breadrobber\src\test.ui'
#
# Created: Mon Apr 01 22:19:05 2013
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
        Dialog.resize(400, 300)
        self.checkBox = QtGui.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(20, 30, 72, 17))
        self.checkBox.setStyleSheet(_fromUtf8("color: rgb(0, 85, 0);\n"
""))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.scrollArea = QtGui.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(20, 70, 111, 91))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 91, 200))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 200))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.checkBox_5 = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_5.setGeometry(QtCore.QRect(11, 80, 72, 17))
        self.checkBox_5.setStyleSheet(_fromUtf8("color: rgb(0, 85, 0);\n"
""))
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.checkBox_2 = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_2.setGeometry(QtCore.QRect(11, 11, 72, 17))
        self.checkBox_2.setStyleSheet(_fromUtf8("color: rgb(0, 85, 0);\n"
""))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.checkBox_3 = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_3.setGeometry(QtCore.QRect(11, 34, 72, 17))
        self.checkBox_3.setStyleSheet(_fromUtf8("color: rgb(0, 85, 0);\n"
""))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.checkBox_4 = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_4.setGeometry(QtCore.QRect(11, 57, 72, 17))
        self.checkBox_4.setStyleSheet(_fromUtf8("color: rgb(0, 85, 0);\n"
""))
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.checkBox_6 = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_6.setGeometry(QtCore.QRect(11, 103, 72, 17))
        self.checkBox_6.setStyleSheet(_fromUtf8("color: rgb(0, 85, 0);\n"
""))
        self.checkBox_6.setObjectName(_fromUtf8("checkBox_6"))
        self.checkBox_7 = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_7.setGeometry(QtCore.QRect(11, 126, 72, 17))
        self.checkBox_7.setStyleSheet(_fromUtf8("color: rgb(0, 85, 0);\n"
""))
        self.checkBox_7.setObjectName(_fromUtf8("checkBox_7"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.checkBox.setText(_translate("Dialog", "CheckBox", None))
        self.checkBox_5.setText(_translate("Dialog", "CheckBox", None))
        self.checkBox_2.setText(_translate("Dialog", "CheckBox", None))
        self.checkBox_3.setText(_translate("Dialog", "CheckBox", None))
        self.checkBox_4.setText(_translate("Dialog", "CheckBox", None))
        self.checkBox_6.setText(_translate("Dialog", "CheckBox", None))
        self.checkBox_7.setText(_translate("Dialog", "CheckBox", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

