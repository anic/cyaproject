# -*- coding: utf8 -*-
import socket

class fsconnection:
    
    PORT_START = 8080
    
    def check_port(self, porttry=10):
        for i in range(porttry): 
            port = self.PORT_START + i
            sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sk.settimeout(1)
            try:
                sk.connect(('localhost', port))  
            except Exception:
                return port
            sk.close()
        
        return -1
    
    def is_listening(self,port):
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sk.settimeout(1)
        try:
            sk.connect(('localhost', port))  
        except Exception:
            return False
        sk.close()
        return True
    
    def check_netuse(self, target, name, password):
        import os
        #清空所有链接
        cmd = 'net use * /delete /y'
        os.system(cmd)
        
        #指定新链接
        cmd = u'net use {0} /User:{1} {2} /PERSISTENT:YES'.format(target, name, password)
        hresult =  os.system(cmd)
        if hresult == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    c = fsconnection()
#    c.check_port()
    if c.check_netuse('\\\\10.244.113.83','GZIAP\\chengyaoan','cheng!@#$5'):
        print 'good!'


