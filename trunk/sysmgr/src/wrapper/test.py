# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'http.ui'
#
# Created: Thu Sep 01 16:54:32 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_HttpWidget(object):
    def setupUi(self, HttpWidget):
        HttpWidget.setObjectName(_fromUtf8("HttpWidget"))
        HttpWidget.resize(400, 300)
        HttpWidget.setWindowTitle(QtGui.QApplication.translate("HttpWidget", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.webView = QtWebKit.QWebView(HttpWidget)
        self.webView.setGeometry(QtCore.QRect(60, 30, 300, 200))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.url = QtGui.QLineEdit(HttpWidget)
        self.url.setGeometry(QtCore.QRect(30, 240, 161, 31))
        self.url.setObjectName(_fromUtf8("url"))
        self.reload = QtGui.QPushButton(HttpWidget)
        self.reload.setGeometry(QtCore.QRect(260, 250, 75, 23))
        self.reload.setText(QtGui.QApplication.translate("HttpWidget", "reload", None, QtGui.QApplication.UnicodeUTF8))
        self.reload.setObjectName(_fromUtf8("reload"))

        self.retranslateUi(HttpWidget)
        QtCore.QMetaObject.connectSlotsByName(HttpWidget)

    def retranslateUi(self, HttpWidget):
        pass

from PyQt4 import QtWebKit

import sys

from PyQt4 import QtCore, QtGui


class httpWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(httpWidget, self).__init__(parent)
        self.ui = Ui_HttpWidget()
        self.ui.setupUi(self)
        
        L = self.layout()
        #L.setMargin(0)
        #self.ui.horizontalLayout.setMargin(5)
        
        url = 'http://www.baidu.com'
        self.ui.url.setText(url)
        
        #self.ui.webView.setUrl(QtCore.QUrl(url))
        
        #self.ui.back.setEnabled(False)
        #self.ui.next.setEnabled(False)
        
        #QtCore.QObject.connect(self.ui.back, QtCore.SIGNAL("clicked()"),\
        #                self.back)
        #QtCore.QObject.connect(self.ui.next, QtCore.SIGNAL("clicked()"),\
        #                self.next)
        QtCore.QObject.connect(self.ui.url, QtCore.SIGNAL("returnPressed()"),\
                        self.url_changed)
        QtCore.QObject.connect(self.ui.webView, QtCore.SIGNAL("linkClicked(const QUrl&)"),\
                        self.link_clicked)
        QtCore.QObject.connect(self.ui.webView, QtCore.SIGNAL("urlChanged(const QUrl&)"),\
                        self.link_clicked)
        QtCore.QObject.connect(self.ui.webView, QtCore.SIGNAL("loadProgress(int)"),\
                        self.load_progress)
        QtCore.QObject.connect(self.ui.webView, QtCore.SIGNAL("loadFinished(bool)"),\
                        self.load_finished)                        
        QtCore.QObject.connect(self.ui.webView, QtCore.SIGNAL("titleChanged(const QString&)"),\
                        self.title_changed)
        QtCore.QObject.connect(self.ui.reload, QtCore.SIGNAL("clicked()"),\
                        self.reload_page)
        #QtCore.QObject.connect(self.ui.stop, QtCore.SIGNAL("clicked()"),\
        #                self.stop_page)
        
        QtCore.QMetaObject.connectSlotsByName(self)
        #开始下载
        self.ui.webView.setUrl(QtCore.QUrl(url))
        
    def url_changed(self):
        page = self.ui.webView.page()
        history = page.history()
        #if history.canGoBack():
        #    self.ui.back.setEnabled(True)
        #else:
        #    self.ui.back.setEnabled(False)
            
        #if history.canGoForward():
        #    self.ui.next.setEnabled(True)
        #else:
        #    self.ui.next.setEnabled(False)
            
        url = self.ui.url.text()
        self.ui.webView.setUrl(QtCore.QUrl(url))
        
    def stop_page(self):
        self.ui.webView.stop()
        
    def title_changed(self, title):
        self.setWindowTitle(title)
        
    def reload_page(self):
        self.ui.webView.setUrl(QtCore.QUrl(self.ui.url.text()))
        
    def link_clicked(self, url):
        page = self.ui.webView.page()        
        #self.__setHistButtonState(page, self.ui.back, self.ui.next)
            
        self.ui.url.setText(url.toString())
        
    def load_progress(self, load):
        page = self.ui.webView.page()
        #if load == 100:
        #    self.ui.stop.setEnabled(False)
        #else:
        #    self.ui.stop.setEnabled(True)
        
    def load_finished(self, load):
        #page = self.ui.webView.page()
        #if load == 100:
        #    self.ui.stop.setEnabled(False)
        #else:
        #    self.ui.stop.setEnabled(True)  
        if load == True:   
            reply = QtGui.QMessageBox.question(self, 'Message',"Download fisnished!Are you sure to quit?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
   
        self.close()
        
    def back(self):
        page = self.ui.webView.page()
        #self.__setHistButtonState(page, self.ui.back, None)
        history = page.history()
        history.back()
            
    def next(self):
        page = self.ui.webView.page()
        history = page.history()
        history.forward()
        
        #self.__setHistButtonState(page, None, self.ui.next)
          
    #control the navigator buttons enability
    def __setHistButtonState(self, page, back, next):
        history = page.history()
        
        #if back is not None:
        #    if history.canGoBack():
        #        back.setEnabled(True)
        #    else:
        #        back.setEnabled(False)
            
        #if next is not None:
        #    if history.canGoForward():
        #        next.setEnabled(True)
        #    else:
        #        next.setEnabled(False)
        
            
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = httpWidget()
    #隐藏界面
    myapp.show()
    sys.exit(app.exec_())
