# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import re, time
from Ui_login import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from facade import *

class LoginDlg(QDialog, Ui_Dialog):
    
    def __init__(self, parent=None):
        super(LoginDlg, self).__init__()
        self.setupUi(self)
        self.setFixedSize(200, 125)
        self.buttonBox.button(QDialogButtonBox.Ok).setText(u"确定");
        self.buttonBox.button(QDialogButtonBox.Cancel).setText(u"取消");