# -*- coding: utf8 -*-
import socket
#import os
import subprocess

class FsConnection:
    
    #启动端口
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
    
    #检查端口是否在监听
    def is_listening(self, port):
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sk.settimeout(1)
        try:
            sk.connect(('localhost', port))  
        except Exception:
            return False
        sk.close()
        return True
    
    #提取路径中的IP
    def extractIp(self, target):
        start = target.find('\\\\')
        if start == -1:
            tmp = target
        else:
            tmp = target[2:]
        
        end = tmp.find('\\')
        if end == -1:
            ip = tmp
        else:
            ip = tmp[:end]
            
        return ip
    
    #检查远程连接
    def check_netuse(self, target, name, password):
        
        #先使用ping命令确认目标存在,测试500ms
        ip = self.extractIp(target)
        code, msg = CommandTool().execute('ping {0} -n 1 -w 500'.format(ip))
        if code != 0 :
            print msg
            return False

        #清空所有链接
        cmd = 'net use * /delete /y'
#        os.system(cmd)
        CommandTool().execute(cmd)
        
        
        #原来的方法
        #命令行需要转译"^"
        #password = password.replace('^', '^^')
        #cmd = u'net use {0} /User:{1} {2} /PERSISTENT:YES'.format(target, name, password)
        #hresult = os.system(cmd)
        
        #指定新链接
        cmd = u'net use {0} /User:{1} {2} /PERSISTENT:YES'.format(target, name, password)
        hresult, msg = CommandTool().execute(cmd)
        
        #操作成功
        if hresult == 0:
            return True
        else:
            #这种情况也是允许的 
            #发生系统错误 1219。
            #不允许一个用户使用一个以上用户名与一个服务器或共享资源的多重连接。中断与此服务器或共享资源的所有连接，然后再试一次...
            if msg.find('1219') != -1:
                return True
            
            return False

    def copyFile(self, sourceFile, targetFile): 
        open(targetFile, "wb").write(open(sourceFile, "rb").read())
         
#http://blog.csdn.net/wuwangyingzhong/article/details/6002055
#http://blog.csdn.net/menglei8625/article/details/7494094

#用于执行控制台命令的类
class CommandTool:
    
    def __init__(self):
        self.log = open('command.log', 'w')
        if self.log == None:
            print('Open command.log failed')
        
    def __del__(self):
        if self.fdp:
            self.fdp.kill()
        if self.log:
            self.log.close()
    
    #执行命令        
    def execute(self, command):
        print command
        
        msg = ''
        self.fdp = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #堵塞等待
        self.fdp.wait()
        
        code = self.fdp.returncode
        #返回正确读取stdout
        if code == 0 or code == 1:
            out = self.fdp.stdout
        else:
            out = self.fdp.stderr
        
        for line in out:
            try:
                wline = line.decode("gb2312")
            except:
                wline = line
            msg += wline
            self.log.write(wline)
            self.log.flush()
            
        self.fdp = None
        
        return code, msg

if __name__ == '__main__':
    c = FsConnection()
#    c.copyFile(u'\\\\10.244.113.83\\规划建设室\\个人目录\\业务一组\\程曜安\\system.mdb', 'F:\\system.mdb')
#    c.check_port()
#    if c.check_netuse('\\\\10.244.113.83', 'GZIAP\\chengyaoan', 'cheng123$%^'):
    if c.check_netuse('\\\\127.0.0.1\\规划建设室\\个人目录\\业务一组\\程曜安\\system.mdb', 'GZIAP\\chengyaoan', 'cheng123$%^'):
        print 'good!'
    else:
        print 'fail'

#    nd = CommandTool().execute('net use \\\\10.244.113.83 /User:GZIAP\\chengyaoan cheng123$%^')
#    nd = CommandTool().execute(['net', 'use', '\\\\10.244.113.83', '/User:GZIAP\\chengyaoan', 'cheng123$%^'])
#    nd = CommandTool().execute(['ping','xqp2.gz.gmcc.net','-n','1'])
#    nd = CommandTool().execute(['net', 'use', '\\\\10.244.113.83', '/User:GZIAP\\chenhu', 'guihua123#'])
#    print nd

#    import commands
#    code, msg = commands.getstatusoutput(' ping xqp2.gz.gmcc.net ')
#    print code
#    print msg.decode('gb2312')

#    from subprocess import *
#    p = Popen("dir", shell=True, stdout=PIPE, stderr=PIPE)
#    p.wait()
#    print p.returncode
#    if p.returncode != 0:
#        print "Error."

