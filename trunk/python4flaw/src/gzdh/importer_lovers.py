# -*- coding:utf-8 -*-

import MySQLdb, re, filesearch
import time
import datetime

def saveAccessLog(datetime, counts):
    
    db = MySQLdb.connect(host="localhost", user="root", passwd="chengyaoan", db="gzdh")
    cur = db.cursor()
    
    #execute an sql query
    cur.execute("select * from lovers_summary where time = %s", (datetime))
    one = cur.fetchone()
    
    print counts, datetime
    if one is None:
        cur.execute("""insert into lovers_summary(`load`,`order`,info,`query`,time) values
        (%s,%s,%s,%s,%s)""",
        (counts[0], counts[1], counts[2],counts[3], datetime))
    else:
        cur.execute("""update lovers_summary set `load` = %s, `order` = %s , info = %s , `query` = %s where time = %s""",
          (counts[0], counts[1], counts[2], counts[3], datetime))
    
    cur.close ()
    db.commit()
    db.close()

        
        
def readAccessLog(filename):
    LOVERS_LOAD = re.compile(r"/gzdh/loversNumber.jsp")
    LOVERS_ORDER = re.compile(r"/gzdh/loveNumberOrder.jsp") #查订单
    LOVERS_INFO = re.compile(r"/gzdh/loversNumberInfo.jsp") #填写订单的
    LOVERS_QUERY = re.compile(r"/gzdh/client/love/getLoveNumber.do") #查询号码的
    
# /gzdh/client/love/getLoveOrder.do
#POST /gzdh/client/love/getNumberOrderInfo.do #填写订单提交
#POST /gzdh/client/love/saveLoveNumberOrder.do #真正提交订单
 
    patterns = [LOVERS_LOAD, LOVERS_ORDER, LOVERS_INFO, LOVERS_QUERY]
    
    table = {}
    
    filereg = re.compile(r'\d{4}-\d{2}-\d{2}')
    fs = filereg.findall(filename)
    
    if not fs is None:
        date = time.strptime(fs[0], "%Y-%m-%d")
        d = datetime.datetime(date[0], date[1], date[2])
        for i in range(0, 24):
            a = datetime.datetime(d.year, d.month, d.day, i, 0, 0)    
            strdate = a.strftime("%Y-%m-%d %H:%M:%S")
            table[strdate] = [0 for col in range(len(patterns) + 1)]
    
    print table
    
    reg = re.compile(r'\[(.*?)\]')
    linecount = 0
    
    for line in open(filename):
        #211.139.145.139 - - [30/Sep/2012:03:41:25 +0800] "GET /gzdh/client/snPhone/searchBeautifulNumber.do HTTP/1.1" 200 5739
        aline = line.strip()
        
        
        linecount += 1
        if linecount % 1000 == 0:
            print 'line count:', linecount
        
        times = re.findall(reg, aline)
        d = parseAccessLogTime(times[0])
        strdate = d.strftime("%Y-%m-%d %H:%M:%S")
        
        if not table.has_key(strdate):
            continue
       
        counts = table[strdate]
        counts_len = len(counts)
        counts[counts_len - 1] = counts[counts_len - 1] + 1
        for i in range(0, len(patterns)):
            m = patterns[i].search(aline)
            if m is not None:
                counts[i] = counts[i] + 1
                break
    
    for current in table:
        counts = table[current]
        saveAccessLog(current, counts)

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
    
    files = filesearch.search("*.txt", 'F:/fwdh_logs/')
    for f in files:
        if FILE_TYPE_ACCESSLOG.search(f) is not None:
            readAccessLog(f)

#    saveAccessLog('2013-02-19 01:00:00', [32, 3, 11, 124])
    
