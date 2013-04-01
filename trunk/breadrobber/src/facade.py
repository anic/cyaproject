# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import mechanize, datetime,re
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Facade(QObject):
    sinOutMsg = pyqtSignal(str)
    
    def __init__(self, proxy={}):
        super(Facade, self).__init__() 
        
        #初始化浏览器
        br = mechanize.Browser()
        #内网不需要代理;设置代理是为了可以用fiddle进行监控
        br.set_proxies(proxy)
        self.br = br 
    
    def debug(self,text):
#        try:
#            f = open('log.txt', 'a')
#            f.write(unicode(str(text)) + '\n')
#            f.close()
#        except Exception,ex:
#            print ex
        pass
    
    def msg(self, text):
        strMsg = unicode('{0} {1}'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                  , unicode(str(text))))
        print strMsg
        
        try:
            f = open('log.txt', 'a')
            f.write(strMsg + '\n')
            f.close()
        except Exception,ex:
            strMsg = strMsg + '\r\n' + unicode(str(ex)) 

        self.sinOutMsg.emit(strMsg)
    
    #如果返回库存数
    def checkProductVault(self, id):
        url = str.format('http://ygjy.gz.gmcc.net/gzxz/ebusiness/portal/directbuy!toBirectbuyInfoPage.action?merchandiseCode={0}&&num=1&&type=undefined'
                         , id)
        try:
            self.br.open(url)
            html = self.br.response().read()
            
            #<script>alert('该商品库存不足!暂时无法购买!');history.go(-1);</script>
            if html.find('history.go(-1);</script>') != -1:
                return 0 #empty
            else:
                pattern = re.compile(r'商品库存：\W*<span class="fRed fb">([\d.]+)')
                match = pattern.search(html)
                if match:
                    stock = int(float(match.groups()[0]))
                else:
                    stock = 0
                
                return stock
        except Exception, e:
            self.msg(e)
            return 0
    
    def performLogin(self, username, password):    
        urlLogin = 'http://ygjy.gz.gmcc.net/gzxz/ebusiness/admin/vmember!login.action'
        #请求登录页面
        try:
            self.br.open(urlLogin)
            self.msg('可访问登录页面，网络畅通')
            
            #填入登录信息
            self.br.select_form(name="loginform")
            self.br['username'] = username
            self.br['password'] = password
            self.br.submit()
            html = self.br.response().read()
            
            #验证登录成功
            loginSuccess = html.find('/gzxz/index.html') != -1
            return loginSuccess
        except Exception, ex:
            self.msg(ex)
            return False
            
    def getProductList(self):
        #获取商品列表
        result = []
        
        try:
            urlProductList = 'http://ygjy.gz.gmcc.net/gzxz/ebusiness/admin/vmerchandist!executeSearch.action?svo.sortId=11'
#            urlProductList = 'http://ygjy.gz.gmcc.net/gzxz/ebusiness/admin/vmerchandist!executeSearch.action'
            self.br.open(urlProductList)
            contentHtml = self.br.response().read()
            
            self.debug(contentHtml)
            
            #<a href="/gzxz/M000127000011.html" target="_blank"><span class="goodscolor">（金海）东北大馒头</span></a>
            import re
            pattern = re.compile(r'<a href="/gzxz/(\w+)\.html" target="_blank"><span class="goodscolor">([^<]+)</span></a>')
            matches = re.findall(pattern, contentHtml)
            for m in matches:
                self.msg(m[0] + " " + m[1])
                result.append({'id':m[0], 'name':m[1]}) 
        except Exception, ex:
            self.msg(ex)
        
        return result

if __name__ == '__main__':
    facade = Facade()
    facade.performLogin('chengyaoan', 'cya!@#45')
#    facade.getProductList()
    
#    facade.msg('hello')
#    facade.msg('你好')
#    facade.msg(u'你好')
#    facade.msg({'id':1, 'name':'你好'})
#    print facade.performLogin('chengyaoan', 'cya!@#a45')
#    facade.getProductList()
#    result = facade.checkProductVault('M000127000015')
#    print 'M000127000015',result
    result = facade.checkProductVault('M000127000025')
    print 'M000127000025',result

#    input = ''' 商品分类：点心坊<br>
#    商品库存： 
#                             
#                            <span class="fRed fb">11.0&nbsp;个</span>
#                             
#                             
#                        <br>
#   每天最大购买数量：
#                       
#                           <span class="fRed fb">10.0&nbsp;个</span>
#                       
#                       
#                 <br>
#   今天已经订购数量：
#                    <span class="fRed fb">0.0&nbsp;个</span>
#                    <br>
#   商品状态： 
#                             
#                            正常购买
#                            
#                             
#                       </ul>'''

#    import re                       
#    pattern = re.compile(r'商品库存：\W*<span class="fRed fb">([\d.]+)')
#    
#    print pattern.search(input).groups()
#    print int(float(pattern.search(input).groups()[0]))


