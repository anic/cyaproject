# -*- coding: utf-8 -*-
import web
#全局用户名称
global _LOGIN_USER
global _EDITABLE
global _MODE

class SysBase():
    
    def __init__(self):
        pass
    
    #获得render
    def render(self):
        if self.isEditable():
            str_editable = '可写'
        else:
            str_editable = '只读'
            
        if self.getMode() == 'local':
            str_mode = '离线'
        else:
            str_mode = '在线'
        
        render = web.template.render('templates/', base='layout',
                                     globals={'LOGIN_USER':_LOGIN_USER,
                                              'MODE':str_mode,
                                              'EDITABLE':str_editable})
        return render

    #获得当前登录用户
    def loginUser(self):
        return _LOGIN_USER
    
    def getMode(self):
        try:
            return _MODE
        except:
            return "local"
    
    #数据库是否可写
    def isEditable(self):
        try:
            return _EDITABLE
        except:
            return False
