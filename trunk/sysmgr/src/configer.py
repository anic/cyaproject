# -*- coding: utf-8 -*-
import ConfigParser

class config:
    
    param = {}
    
    #保存到配置文件ini
    def loadFromIni(self):
        config = ConfigParser.ConfigParser()
        config.readfp(open('config.ini'))
        self.param['remotepath'] = config.get("DatabaseInfo", "remotepath")
        self.param['location'] = config.get("DatabaseInfo", "location")
        self.param['localpath'] = config.get("DatabaseInfo", "localpath")

        self.param['username'] = config.get("ConnectionInfo", "username")
        self.param['password'] = config.get("ConnectionInfo", "password")
        

    def saveToIni(self, param):
#        try:
#            
#            if param['user'] != '':
#                code = Code(unicode(param['user']))
#                encrypted = code.encode(unicode(param['password']))
#            else:
#                encrypted = param['password']
#            
#            
#            config = ConfigParser.ConfigParser()
#            
#            # set a number of parameters
#            config.add_section("UserInfo")
#            config.set("UserInfo", "user", param['user'])
#            config.set("UserInfo", "password", encrypted)
#    
#            config.write(open('config.ini', "w"))
#        except Exception, ex:
#            self.facade.msg(ex)
        pass
            
def instance():
        global inst
        try:
            inst
        except:
            inst = config()
            inst.loadFromIni()
        return inst
