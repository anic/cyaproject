# -*- coding: utf-8 -*-
import ConfigParser

from encrypt import Code
class Config:
    
    param = {}
    facade = None
    
    def __init__(self, facade):
        self.facade = facade
    
    #保存到配置文件ini
    def loadSysConfigFromIni(self):
        
        try:
            config = ConfigParser.ConfigParser()
            config.readfp(open('system.ini'))
            
            
            self.param['remotepath'] = config.get("Database", "remotepath")
            self.param['localpath'] = config.get("Database", "localpath")
    
                   
            self.param['sysuser'] = config.get("Connection", "sysuser")
            self.param['syspassword'] = config.get("Connection", "syspassword")
            self.param['scope'] = config.get("Connection", "scope")
        except Exception, ex:
            self.facade.msg(ex)
    
    
    #保存到配置文件ini
    def loadUserFromIni(self):
        try:
            config = ConfigParser.ConfigParser()
            config.readfp(open('config.ini'))
            user = config.get("UserInfo", "user")
            password = config.get("UserInfo", "password")
            
            if user != '':
                code = Code(user)
                password = code.decode(password)
                #如果解析错了，则重置为空
                if password is None:
                    password = ''
            
            self.param['user'] = user
            self.param['password'] = password
        except:
            self.param['user'] = ''
            self.param['password'] = ''


    def saveUserToIni(self, param):
        try:
            
            if param['user'] != '':
                code = Code(unicode(param['user']))
                encrypted = code.encode(unicode(param['password']))
            else:
                encrypted = param['password']
            
            
            config = ConfigParser.ConfigParser()
            
            # set a number of parameters
            config.add_section("UserInfo")
            config.set("UserInfo", "user", param['user'])
            config.set("UserInfo", "password", encrypted)
    
            config.write(open('config.ini', "w"))
        except Exception, ex:
            self.facade.msg(ex)
            
