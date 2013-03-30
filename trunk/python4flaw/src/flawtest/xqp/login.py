import urllib2, cookielib, mechanize
br = mechanize.Browser()
#    br.addheaders = [('User-agent', 'Mozilla/4.0(compatible; MSIE 7.0b; Windows NT 6.0)')]
br.open('http://xqp2.gz.gmcc.net/')
response = br.response()
print response.read()