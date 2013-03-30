import urllib2, cookielib, mechanize

#g_cookiejar = cookielib.CookieJar()
#g_urlopener = urllib2.build_opener(urllib2.HTTPCookieProcessor(g_cookiejar))
#urllib2.install_opener(g_urlopener)


br = mechanize.Browser()
#    br.addheaders = [('User-agent', 'Mozilla/4.0(compatible; MSIE 7.0b; Windows NT 6.0)')]
br.open('http://itsd.gz.gmcc.net/')
response = br.response()

print response.read()