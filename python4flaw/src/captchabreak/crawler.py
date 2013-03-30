# -*- coding:utf-8 -*-
import urllib2, urllib, os, cookielib
from crack import crackCaptcha
from bs4 import BeautifulSoup
from time import sleep

LOGIN_URL = 'http://gd.10086.cn/gzdh/client/snLogin/login.do' 
SEARCH_URL = 'http://gd.10086.cn/gzdh/client/snPhone/searchBeautifulNumber.do'
G_COOKIES = ''
g_cookiejar = None
g_urlopener = None

def openurl(req):
    return urllib2.urlopen(req)

#下载图片
def download_img(url, dist, min_size):
#    print "download begin..."
    
    #此方式判断图片的大小太浪费了
    #if len(urllib2.urlopen(im).read()) < min_size:
    #continue
    #这种方式先拉头部，应该好多了，不用再下载一次
    headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
               'Cookie':G_COOKIES}
    req = urllib2.Request(url, headers=headers)
    connection = openurl(req)
    
    if int(connection.headers.dict['content-length']) < min_size:
        print 'download fail'
        return
    
    urllib.urlretrieve(url, dist, None)
    print "Done: ", dist
    print "download end..."

def getCode(url):
    save_path = os.path.abspath("./downlaod")
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    
    filename = 'code.jpg'
    dist = os.path.join(save_path, filename)
    
    code = ''
    #如果识别到是4个字符，则判断为正确识别
    for i in xrange(0, 10):
        download_img(url, dist, 8)
        code = crackCaptcha(dist)
        if isCode(code):
            return code
        sleep(1)
        
    return ''

def login(username, password):
    global G_COOKIES
    code = getCode('http://gd.10086.cn/gzdh/loginRandom')
    
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
    url=LOGIN_URL,
    data=postdata,
    headers=headers
    )
    
    print 'Try login with code ', code
    connection = openurl(req)
#    print connection.headers
#    print G_COOKIES
    
    result = connection.read()
    soup = BeautifulSoup(result, from_encoding="gbk")
    html = soup.prettify()
    #for debug
    #print html
    
    print g_cookiejar
    
    if html.find(u'您好') != -1:
        print 'Login Success'
        return True
    else:
        print 'Login Fail'
        return False

def extractNumber(result):
    import re
    reg = re.compile(r'value="([\d]{11})"')
    match = reg.findall(result)
    print match
    output = open('number.log', 'w')
    output.write(",".join(match))
    output.close()

def isCode(code):
    import re    
    reg = re.compile(r'^[A-Z0-9]{4}$')
    match = re.match(reg,code)
    return match != None

def searchBeautifulNumber():
    
    
    
    #构造浏览器头
#    headers = {'Accept':'*/*',
#               'Accept-Charset':'GBK,utf-8;q=0.7,*;q=0.3',
#               'Accept-Encoding':'gzip,deflate,sdch',
#               'Accept-Language':'zh-CN,zh;q=0.8',
#               'Connection':'keep-alive',
##               'Content-Length':34,
#               'Content-Type':'application/x-www-form-urlencoded',
#               'Host':'gd.10086.cn',
#               'Origin':'http://gd.10086.cn',
#               'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
#               'X-Requested-With':'XMLHttpRequest'}
    headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    req = urllib2.Request(url='http://gd.10086.cn/gzdh/client/snPhone/loadBeautifulNumber.do',
                          headers=headers)
    connection = openurl(req)
    result = connection.read()
    print connection.headers
#    print result
#    soup = BeautifulSoup(result)
#    print soup
#    print connection.headers
    return

    code = getCode('http://gd.10086.cn/gzdh/searchRandom')
    postdata = urllib.urlencode({
    'aa':1,
    'startNum':'139',
    'requestCode':code
    })
    #构造请求
    req = urllib2.Request(
    url=SEARCH_URL,
    data=postdata,
    headers=headers
    )
    print req.get_method()
    
    connection = openurl(req)
    result = connection.read()
    print connection.headers
    soup = BeautifulSoup(result, from_encoding="gbk")
    html = soup.prettify()
    print extractNumber(html)

if __name__ == '__main__':
    
    g_cookiejar = cookielib.CookieJar()
    g_urlopener = urllib2.build_opener(urllib2.HTTPCookieProcessor(g_cookiejar))
    urllib2.install_opener(g_urlopener)

    while not login('test1', 'gmcc123!@#'):
        sleep(10)
    
    searchBeautifulNumber()

#    extractNumber(""" </tr>
# <tr>
#  <td>
#   <input id="photoNumber" name="photoNumber" onclick="CheckClick(this)" type="checkbox" value="13922715911"/>
#   13922715911
#  </td>
#  <td class="red">
#   500
#  </td>
#  <td>
#   128元及以上
#  </td>
#  <td>
#   <input id="photoNumber" name="photoNumber" onclick="CheckClick(this)" type="checkbox" value="13924059700"/>
#   13924059700
#  </td>""")


#http://gd.10086.cn/gzdh/client/snLogin/login.do
#userId:test1
#password:gmcc123!@#
#authCode:sv17
