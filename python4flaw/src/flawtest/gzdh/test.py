# -*- coding:utf-8 -*-
import sys
type = sys.getfilesystemencoding()
print str.decode('UTF-8').encode(type)

import mechanize, urllib, urllib2
from urllib2 import URLError, HTTPError
br = mechanize.Browser()
#br.set_proxies({"http": "10.243.184.38:8081"})
br.set_proxies({"http": "127.0.0.1:8889"})
#br.open('http://gd.10086.cn/gzdh/robot/mzone_fallin.jsp')
#response = br.response()
import socket
socket.setdefaulttimeout(5)


#depth存在注入
params = urllib.urlencode({'parentCode':'44010000',
                           'depth':'0'})
#                         'depth':'2'})
print params
                         
req = urllib2.Request("http://gd.10086.cn/gzdh/client/serviceConfig/searchOrderArea.do"
                        , params)



try:
    response = urllib2.urlopen(req)
    s = response.read()
    print s.decode('gbk').encode('utf8') 
except urllib2.URLError, e:
    print e
    
    
#response = br.post('http://gd.10086.cn/gzdh/client/serviceConfig/searchOrderArea.do?parentCode=44010000&depth=1%2B1')
#http://gd.10086.cn/gzdh/client/serviceConfig/searchOrderArea.do?parentCode=44010000&depth=0%2B0%2B0%2B2