# -*- coding:utf-8 -*-

import MySQLdb, re, filesearch
import time
import datetime

def saveAccessLog(datetime, ip, table):
    
    db = MySQLdb.connect(host="localhost", user="root", passwd="chengyaoan", db="gzdh")
    cur = db.cursor()
    
    #execute an sql query
    cur.execute("select * from accesslog_code where time = %s and ip = %s", (datetime, ip))
    one = cur.fetchone()
    
    try:
        if one is None:
            cur.execute("""insert into accesslog_code(ip,time,code200,code302,code304,code404,code500,visitcount) 
            values(%s,%s,%s,%s,%s,%s,%s,%s)""",
            (ip, datetime, table[ip]['200'], table[ip]['302'], table[ip]['304'], table[ip]['404'], table[ip]['500'], table[ip]['visit']))
        else:
            cur.execute("""update accesslog_code set code200 = %s, code302 = %s, code304 = %s,
             code404 = %s, code500 = %s, visitcount = %s where time = %s and ip = %s""",
             (table[ip]['200'], table[ip]['302'], table[ip]['304'], table[ip]['404'], table[ip]['500'], table[ip]['visit'], datetime, ip))
    except:
        print '\nSome error/exception occurred.'
        
    cur.close ()
    db.commit()
    db.close()

        
def readAccessLog(filename):
    
    table = {}
    table['all'] = {'200':0, '301':0, '302':0, '304':0, '404':0, '500':0, 'visit':0}
    
    filereg = re.compile(r'\d{4}-\d{2}-\d{2}')
    fs = filereg.findall(filename)
    
    if not fs is None:
        date = time.strptime(fs[0], "%Y-%m-%d")
        filedate = datetime.datetime(date[0], date[1], date[2])
        
    reg = re.compile(r'\[(.*?)\]')
    visitcount = 0
    
    for line in open(filename):
        #new format:
        #- 157.55.33.18 - - [24/Dec/2012:00:01:27 +0800] "GET /robots.txt HTTP/1.1" 404 -
        #58.248.232.160 211.139.145.139 - - [24/Dec/2012:00:02:55 +0800] "GET /gzdh/search.jsp HTTP/1.1" 200 69825

        #211.139.145.139 - - [30/Sep/2012:03:41:25 +0800] "GET /gzdh/client/snPhone/searchBeautifulNumber.do HTTP/1.1" 200 5739
        aline = line.strip()
        params = aline.split(' ')
        print aline
        
        visitcount += 1
        if visitcount % 1000 == 0:
            print 'line count:', visitcount
        
        times = re.findall(reg, aline)
        linedate = parseAccessLogTime(times[0])
        
        if filedate.day != linedate.day:
            continue 
        
        #存在一些格式不对
        #10.184.6.164, 127.0.0.1,220.181.51.55 211.139.145.139 - - [24/Dec/2012:18:26:02 +0800] "GET /gzdh HTTP/1.0" 302 -
        
        #记录全局信息
        try:
            code = params[9]
            if table['all'].has_key(code):
                table['all'][code] = table['all'][code] + 1
            table['all']['visit'] = table['all']['visit'] + 1
             
            #记录个别IP信息
            ip = params[0]
            if ip == '-':
                continue
            if not table.has_key(ip):
                table[ip] = {'200':0, '301':0, '302':0, '304':0, '404':0, '500':0, 'visit':0}
           
            if table[ip].has_key(code):
                table[ip][code] = table[ip][code] + 1
            table[ip]['visit'] = table[ip]['visit'] + 1 
        except:
            pass    
    
    for attr in table:
        saveAccessLog(filedate.strftime('%Y-%m-%d'), attr, table)
    
def parseAccessLogTime(strtime):
    try:
        date = time.strptime(strtime, "%d/%b/%Y:%H:%M:%S +0800")
        d = datetime.datetime(date[0], date[1], date[2], date[3])
        return d
    except:
        print 'Error:', strtime



if __name__ == '__main__':
    FILE_TYPE_ACCESSLOG = re.compile(r'localhost_access_log')
    FILE_TYPE_FWDHLOG = re.compile(r'fwdh_logs')
    
    files = filesearch.search("*", 'F:/fwdh_logs/')
    for f in files:
        if FILE_TYPE_ACCESSLOG.search(f) is not None:
            readAccessLog(f)
#    readLog('F:/fwdhlogs/localhost_access_log.2012-12-07.txt')
#    saveToDb('2012-12-12 12:00:00', [0, 0, 0, 0, 1])
    

#    ['30/Sep/2012:02:26:22 +0800']
#    reg = re.compile(r'\[(.*?)\]')
#    i = '[30/Sep/2012:07:53:01 +0800] "GET /gzdh?debug=command&expression=%23_memberAccess["allowStaticMethodAccess"]'
#    times = re.findall(reg, i)
#    print times
    
#    date = time.strptime(i, "%d/%b/%Y:%H:%M:%S +0800")
#    print date[0],date[1],date[2],date[3],date[4],date[5]
#    d4 = datetime.datetime(date[0], date[1], date[2], date[3], date[4], date[5])
#    print d4
    
#    d1 = datetime.datetime(2005, 2, 16)
#    d2 = datetime.datetime(2004, 12, 31)
#    print d1,d2 
#    
#    date = '2007-01-01'
#    print type(date)
#
#    date = time.strptime(date,"%Y-%m-%d")
#    print date[0]
#
#    d4 = datetime.datetime(date[0], date[1],date[2])
#    
#    print d4
#    print type(d4)
    
