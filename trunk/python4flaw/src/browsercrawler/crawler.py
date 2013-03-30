import mechanize
LOGIN_URL = 'http://gd.10086.cn/gzdh/client/snLogin/login.do' 
SEARCH_URL = 'http://gd.10086.cn/gzdh/client/snPhone/searchBeautifulNumber.do'

if __name__ == '__main__':
    print 'hello'
    br = mechanize.Browser()
#    br.addheaders = [('User-agent', 'Mozilla/4.0(compatible; MSIE 7.0b; Windows NT 6.0)')]
    br.open(LOGIN_URL)
    response = br.response()
    headers = response.info()  # currently, this is a mimetools.Message
    
    print headers
    print response.read()
    
#    response = mechanize.urlopen("http://gd.10086.cn/gzdh")
#    print response.read()