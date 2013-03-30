# -*- coding:utf-8 -*-
import os, mechanize, urllib2, urllib, cookielib
from crack import crackCaptcha
from bs4 import BeautifulSoup
from time import sleep

class GzdhCrawler():
    
    
    
    def __init__(self):
        #定义常量
        self.LOGIN_URL = 'http://gd.10086.cn/gzdh/client/snLogin/login.do'
        self.SEARCH_NUMBER_URL = 'http://gd.10086.cn/gzdh/client/snPhone/searchBeautifulNumber.do'
        self.LOGIN_CODE = 'http://gd.10086.cn/gzdh/loginRandom' 
        self.SEARCH_CODE = 'http://gd.10086.cn/gzdh/searchRandom'
        
        #构造临时目录保存验证码等
        self.SAVE_PATH = os.path.abspath("./downlaod")
        if not os.path.exists(self.SAVE_PATH):
            os.mkdir(self.SAVE_PATH)
        #浏览器状态保存文件
        self.BROWSER_STATE_PATH = os.path.join(self.SAVE_PATH, 'browser-state.txt')

        #初始化浏览器
        self.br = mechanize.Browser()
#        self.br.set_proxies({"http": "http://10.243.184.38:8081"})
        
        self.cookiejar = cookielib.LWPCookieJar()
        self.br.set_cookiejar(self.cookiejar)
        if os.path.exists(self.BROWSER_STATE_PATH):
            self.cookiejar.load(self.BROWSER_STATE_PATH, True, True)
            print self.cookiejar


    #下载图片
    def download_img(self, url, dist):
        self.br.retrieve(url, dist)
        print "Code download", dist, url

    def getCode(self, url, codelen=4):
        filename = 'code.jpg'
        dist = os.path.join(self.SAVE_PATH, filename)
        
        code = ''
        #如果识别到是4个字符，则判断为正确识别
        for i in xrange(0, 10):
            self.download_img(url, dist)
            code = crackCaptcha(dist)
            if len(code) == codelen:
                return code
            sleep(1)
            
        return ''

    def login(self, username, password):
        code = self.getCode(self.LOGIN_CODE)
        
        #构造登录请求
        postdata = urllib.urlencode({
        'userId':username,
        'password':password,
        'authCode':code
        })
        #构造浏览器头
        headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

        #构造请求
        req = urllib2.Request(
        url=self.LOGIN_URL,
        data=postdata,
        headers=headers
        )
        
        #尝试使用验证码登录
        print 'Try login with code ', code
        self.br.open(req)
        result = self.br.response().read()
        
#        #解析内容
#        soup = BeautifulSoup(result, from_encoding="gbk")
#        html = soup.prettify()
#        
#        #for debug
#        #print html
#    
#        #如果内容中找到欢迎字样，表示成功
#        if html.find(u'您好') != -1:
#            print 'Login Success'
#            return True
#        else:
#            print 'Login Fail'
#            return False

        return self.isLogin()
    
    #检查是否已经登录
    def isLogin(self):
        CHECK_URL = 'http://gd.10086.cn/gzdh/client/snOrder/queryOrder.do'
        self.br.open(CHECK_URL)
        result = self.br.response().read()
        
        #解析内容
        soup = BeautifulSoup(result, from_encoding="gbk")
        html = soup.prettify()
        
        #for debug
        #print html
    
        #如果内容中找到欢迎字样，表示成功
        if html.find(u'您好') != -1:
            print 'Login Success'
            #保存浏览器状态
            self.cookiejar.save(self.BROWSER_STATE_PATH, True, True)
            return True
        else:
            print 'Login Fail'
            return False

    def searchBeautifulNumber(self):
        
        #构造浏览器头
        headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
        req = urllib2.Request(url='http://gd.10086.cn/gzdh/client/snPhone/loadBeautifulNumber.do',
                              headers=headers)
        self.br.open(req)
        print 'load page loadBeautifulNumber.do'
    
        while True:
    
            code = self.getCode(self.SEARCH_CODE)
            postdata = urllib.urlencode({
            'aa':1,
            'startNum':'139',
            'requestCode':code
            })
            #构造请求
            req = urllib2.Request(
            url=self.SEARCH_NUMBER_URL,
            data=postdata,
            headers=headers
            )
            
            response = self.br.open(req)
            result = response.read()
            soup = BeautifulSoup(result, from_encoding="gbk")
            html = soup.prettify()
            
            print html
            if html.rstrip() != '1':
                print 'Search Number Successful'
                break
            
            print 'Search fail,wait for a while'
            sleep(2)
            
            

if __name__ == '__main__':
    c = GzdhCrawler()
    if not c.isLogin():
        while not c.login('test1', 'gmcc123!@#'):
            print 'wait for a while'
            sleep(2)
        

    c.searchBeautifulNumber()
    
#    c.br.open(c.loginUrl)
#    print cj.save(filename, ignore_discard, ignore_expires)

#    while not login('test1', 'gmcc123!@#'):
#        print 'wait for a while'
#        sleep(2)
    
#    searchBeautifulNumber()

#http://gd.10086.cn/gzdh/client/snLogin/login.do
#userId:test1
#password:gmcc123!@#
#authCode:sv17
