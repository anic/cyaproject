import mechanize, re

br = mechanize.Browser()
#br.set_proxies({"http": "127.0.0.1:8889"})
br.open('http://itsd.gz.gmcc.net/')
response = br.response()

#print response.read()

br.select_form(name="form1")

br['txtUserName'] = 'chengyaoan'
br['txtPassword'] = 'cya!@#45'

br.submit()

response = br.response()

html = response.read()
#print html

m = re.search(r'window.location = "/main/default\.aspx";',html,re.M)

br.open('http://itsd.gz.gmcc.net/main/default.aspx')
html = br.response().read()


br.open('http://itsd.gz.gmcc.net/contrib/workflow/pages/searchPrecision.aspx/')
br.select_form('aspnetForm')
br.submit()

response = br.response()
html = response.read()

print html

print '=============='

br.open('http://itsd.gz.gmcc.net/contrib/workflow/pages/searchPrecision.aspx/')
br.select_form('aspnetForm')
br['ctl00$cphBody$textKeyword'] = '%28select+%29'
br.submit()

response = br.response()
html = response.read()

print html