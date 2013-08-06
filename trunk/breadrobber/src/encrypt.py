# -*- coding: utf-8 -*-
'''
    Description: 可逆的加密与解密
    Environment: python2.5.x
    Author:idehong@gmail.com
'''

import os
import sys

class Code(object):
    '''可逆的加密与解密'''
    
    def __init__(self, key="idehong@gmail.com"):
        self.__src_key = key
        self.__key = self.__get_strascii(self.__src_key, True)
    
    def encode(self, value):
        '''加密函数, 加密后为一串数字'''
        return  "%d" % (self.__get_strascii(value, True) ^ self.__key)
    
    def decode(self, pwd):
        '''解密函数'''
        if self.is_number(pwd):
            return self.__get_strascii((int(pwd)) ^ self.__key, False)
        else:
            print 'require number.'
    
    def reset_key(self, key):
        '''重新设置key'''
        self.__src_key = key
        self.__key = self.__get_strascii(self.__src_key, True)
  
#===============================================================================
#        内部调用接口
#===============================================================================

    def __get_strascii(self, value, bFlag):
        if bFlag:
            return self.__get_str2ascii(value) 
        else:
            return self.__get_ascii2str(value)
                      
    def __get_str2ascii(self, value):
        ls = []
        for i in value:
            ls.append(self.__get_char2ascii(i))
        return long("".join(ls))

    def __get_char2ascii(self, char):
        '''获取单个字符的acsii码值'''
        try:
            return "%03.d" % ord(char)
        except (TypeError, ValueError):
            print "key error."
            exit(1)
            
    def __get_ascii2char(self, ascii):
        if self.is_ascii_range(ascii):
            return chr(ascii)
        else:
            print "ascii error(%d)" % ascii
            exit(1)       
    
    def __get_ascii2str(self, n_chars):
        ls = []
        s = "%s" % n_chars
        n, p = divmod(len(s), 3)
        if p > 0:
            nRet = int(s[0 : p])
            ls.append(self.__get_ascii2char(nRet))
       
        pTmp = p
        while pTmp < len(s):
            ls.append(self.__get_ascii2char(int(s[pTmp: pTmp + 3])))
            pTmp += 3
        return "".join(ls)
                
#================================================================================
#        工具接口
#================================================================================
    
    def is_number(self, value):
        try:
            int(value)
            return True
        except (TypeError, ValueError):
            pass
        return False
                
    def is_ascii_range(self, n):
        return 0 <= n < 256
    
    def is_custom_ascii_range(self, n):
        return 33 <= n < 48 or 58 <= n < 126       
        
    
class Usage(object):
    '''
    命令行参数读取与解析
    '''
    
    def __init__(self):
        
        self._clsWork = Code()
        self._args_dic = {'arg_help' : ['-?', '-help'],
                    'arg_p' : ['-p', '-pwd'],
                    'arg_t' : ['-t', '-text'],
                    'arg_k' : ['-k', '-key'],
                    }        
        
    def help(self, *k):
        
        strHelp = "Usage: pwd [-options] [args...] where option include:"
        strHelp += """
        -? -help                    print this help message
        -k <key_str> -p <pwd_str>
        -k <key_str> -t <text_str>"""
        
        print strHelp  
        
    def args(self, argv_ls): 
        '''dispatch command'''  
        
#        print argv_ls
        if len(argv_ls) <= 1 or len(argv_ls) > 5:
            print 'Unrecognized option'
            return
        
        cmd_dic = {}
        curr_cmd = ''
        # control command
        for i, v in enumerate(argv_ls[1:]):
            for j in self._args_dic.items():
                # add command
                if v in j[1] and j[0] not in cmd_dic:
                    curr_cmd = j[0]
                    cmd_dic[curr_cmd] = []
                    break
            else:
                # add argv
                if cmd_dic:
                    cmd_dic[curr_cmd].append(v)            
                     
        # exec command
        if cmd_dic:
            self.exec_cmd(cmd_dic)
        else:
            print 'Unrecognized option'
        
    def exec_cmd(self, cmd_dic):  
        '''exec cmd'''      
        if len(cmd_dic) == 2:
            if 'arg_p' in cmd_dic and 'arg_k' in cmd_dic and len(cmd_dic['arg_p']) == 1 and len(cmd_dic['arg_k']) == 1:
                
                self._clsWork.reset_key(cmd_dic['arg_k'][0])
                print self._clsWork.encode(cmd_dic['arg_p'][0])
                return
            elif 'arg_t' in cmd_dic and 'arg_k' in cmd_dic and len(cmd_dic['arg_t']) == 1 and len(cmd_dic['arg_k']) == 1:
                self._clsWork.reset_key(cmd_dic['arg_k'][0])
                print self._clsWork.decode(cmd_dic['arg_t'][0])
                return
        self.help()
          
           
if __name__ == '__main__':
#    usage = Usage()
#    usage.args(sys.argv)

    code = Code()
    code.reset_key('chengyaoan')
    print code.encode('cya!@#45')


