#! /usr/bin/env python 
# -*- coding: utf-8 -*-


print("Hello, world!")
print "欢迎来到奥运中国!" # 使用中文的例子

import math
print(math.sin(math.pi / 2))
#a = raw_input("Press enter key to close this window");
#print a

# Loops List
a = ['cat', 'window', 'defenestrate']
for x in a:
    print x, len(x)

def sum(a, b):
    return a + b

print '1+2=' + str(sum(1, 2))

a = range(5, 10)
print a


import os
dirs = os.listdir("e:/a/")
for d in dirs:
    print unicode(d, 'gbk') #将dir的内容转换为utf8
    
s = '测试'
print unicode(d, 'gbk')
print unicode(d, 'gbk') == s

from searcher import filesearch
#print os.path.abspath("E:/work/mytask/120521 漏洞扫描/flaws_target/")
#print os.listdir(u"E:/work/mytask/120521 漏洞扫描/flaws_target/")


#for d in filesearch.search("*", u"E:/work/mytask/120521 漏洞扫描/flaws_target/"):
#    print d#unicode(d,'gbk')


from HTMLParser import HTMLParser
class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []
        self.markData = False
 
    def handle_starttag(self, tag, attrs):
        #print "Encountered the beginning of a %s tag" % tag
        self.markData = False
        if tag == "span":
            if len(attrs) == 0: pass
            else:
                for (variable, value)  in attrs:
                    if variable == "class" and value == "f34_":
                        self.markData = True
#                        self.links.append(tag.data)
    
    def handle_data(self, data):
        print data
        if self.markData == True:
            self.links.append(data)

    def handle_endtag(self, tag):
        self.markData = False
 
if __name__ == "__main__":
    html_code = """
    <a href="www.google.com"> google.com</a>
    <A Href="www.pythonclub.org"> PythonClub </a>
    <A HREF = "www.sina.com.cn"> Sina </a>
    """
    hp = MyHTMLParser()
#    html = open(u"E:/flaws_target/0521/内外网互联系统/AppScan_虚拟服务厅_20120517.html").read();
#    print html
#    hp.feed(html)
#    hp.feed(html_code)
#    hp.close()

#    s = u"&#169;"
#    print s.encode("utf-8")
#    print(hp.links)

    import urllib                    
    urlItem = urllib.urlopen("http://www.baidu.com")
    html = urlItem.read()
    html = unicode(html, "gbk")
    hp.feed(html)
    urlItem.close()
    hp.close()
#    urlItem = urllib.urlopen("file://E:/b.html")
#    htmSource = urlItem.read()
#    print unicode(htmSource,"gbk")
#    urlItem.close()

