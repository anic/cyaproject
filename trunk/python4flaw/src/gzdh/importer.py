# -*- coding:utf-8 -*-

import MySQLdb, re, filesearch
import time
import datetime

def saveAccessLog(datetime, counts):
    
    db = MySQLdb.connect(host="localhost", user="root", passwd="chengyaoan", db="gzdh")
    cur = db.cursor()
    
    #execute an sql query
    cur.execute("select * from accesslog_summary where time = %s", (datetime))
    one = cur.fetchone()
    
    counts.append(datetime)
    print counts
    if one is None:
        cur.execute("""insert into accesslog_summary(diy188search,diy188init,diy139search,diy139init,channel188search,
        channel188init,channel139search,channel139init,channel137search,channel137init,robot,visitcount,time) values
        (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
        (counts[0], counts[1], counts[2], counts[3], counts[4], counts[5], counts[6], counts[7], counts[8],
          counts[9], counts[10], counts[11], datetime))
    else:
        cur.execute("""update accesslog_summary set diy188search = %s, diy188init = %s , diy139search = %s, diy139init = %s,
         channel188search = %s, channel188init = %s,channel139search = %s, channel139init = %s, channel137search = %s,
         channel137init = %s , robot = %s,visitcount = %s where time = %s""",
          (counts[0], counts[1], counts[2], counts[3], counts[4], counts[5], counts[6], counts[7], counts[8],
          counts[9], counts[10], counts[11], datetime))
    
    cur.close ()
    db.commit()
    db.close()

def saveFWDH(datetime, counts):
    
    db = MySQLdb.connect(host="localhost", user="root", passwd="chengyaoan", db="gzdh")
    cur = db.cursor()
    
    #execute an sql query
    cur.execute("select * from accesslog_summary where time = %s", (datetime))
    one = cur.fetchone()
    
    counts.append(datetime)
    print counts
    if one is None:
        cur.execute("""insert into accesslog_summary(appdiy188,appdiy139,appchannel188,
        appchannel139,appchannelinit,approbot,appboss,time) values(%s,%s,%s,%s,%s,%s,%s,%s)""", (counts[0], counts[1], counts[2], counts[3], counts[4], counts[5], counts[6], datetime))
    else:
        cur.execute("""update accesslog_summary set appdiy188 = %s, appdiy139 = %s,
         appchannel188 = %s, appchannel139 = %s, appchannelinit = %s, approbot = %s, appboss = %s where time = %s""",
          (counts[0], counts[1], counts[2], counts[3], counts[4], counts[5], counts[6], datetime))
    
    cur.close ()
    db.commit()
    db.close()


def readAppLog(filename):
    APP_DIY139 = re.compile(r'==电子渠道DIY全球通选号功能==')
    APP_DIY188 = re.compile(r'==电子渠道DIY全球通188选号功能==')
    
    APP_CHANNEL139 = re.compile(r'======社会网点【138、139选号】功能===')
    APP_CHANNEL139_INIT = re.compile(r'======初始化社会网点138、139靓号====')
    
    APP_CHANNEL188 = re.compile(r'======社会网点【188选号】功能====')
#    APP_CHANNEL188_INIT = re.compile(r'======初始化社会网点138、139靓号====')

#    APP_CHANNEL137 = re.compile(r'======社会网点【134-137选号】功能====')
#    APP_CHANNEL137_INIT = re.compile(r'======初始化社会网点134-137选号====')
    
    APP_ROBOT = re.compile(r'=======电子渠道使用选号机器人选号=====')
    APP_BOSS = re.compile(r'92007')
    
    table = {}
    filereg = re.compile(r'\d{4}-\d{2}-\d{2}')
    fs = filereg.findall(filename)
    
    if not fs is None:
        date = time.strptime(fs[0], "%Y-%m-%d")
        d = datetime.datetime(date[0], date[1], date[2])
        for i in range(0, 24):
            a = datetime.datetime(d.year, d.month, d.day, i, 0, 0)    
            strdate = a.strftime("%Y-%m-%d %H:%M:%S")
            table[strdate] = [0, 0, 0, 0, 0, 0, 0]
    
    reg = re.compile(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}')
    
    patterns = [ APP_DIY188, APP_DIY139, APP_CHANNEL188, APP_CHANNEL139, APP_CHANNEL139_INIT, APP_ROBOT, APP_BOSS]
    linecount = 0
    
    for line in open(filename):
        aline = line.strip()
        #[INFO ] 2012-12-06 16:49:21 [com.client.common.ServiceUse][600] =======电子渠道全球通选号调用boss=============
        
        linecount += 1
        if linecount % 1000 == 0:
            print 'line count:', linecount
        
        times = re.findall(reg, aline)
        if len(times) == 0:
            continue
    
        d = parseFWDHTime(times[0])
        strdate = d.strftime("%Y-%m-%d %H:%M:%S")
        
        if not table.has_key(strdate):
            continue
        
        counts = table[strdate]
        for i in range(0, len(patterns)):
            m = patterns[i].search(aline)
            if m is not None:
                counts[i] = counts[i] + 1
                break
            
    for current in table:
        counts = table[current]
        saveFWDH(current, counts)
        
        
def readAccessLog(filename):
    DIY188_SEARCH = re.compile(r"/gzdh/client/phone/search188Number.do")
    DIY188_INIT = re.compile(r"/gzdh/search188Number.jsp")
    
    DIY139_SEARCH = re.compile(r"/gzdh/client/phone/searchNumber.do")
    DIY139_INIT = re.compile(r'/gzdh/client/phone/loadnumber.do')
    
    CHANNEL139_SEARCH = re.compile(r"/gzdh/client/snPhone/searchBeautifulNumber.do")
    CHANNEL139_INIT = re.compile(r"/gzdh/client/snPhone/loadBeautifulNumber.do")
    
    CHANNEL137_SEARCH = re.compile(r"/gzdh/client/snPhone/searchNumber.do")
    CHANNEL137_INIT = re.compile(r"/gzdh/client/snPhone/loadnumber.do")
    
    CHANNEL188_SEARCH = re.compile(r"/gzdh/client/snPhone/search188Number.do")
    CHANNEL188_INIT = re.compile(r"/gzdh/socialNetwork/search188Number.jsp")
    
    ROBOT = re.compile(r"/gzdh/client/selectionRobot/getNumber.do")
    
    patterns = [DIY188_SEARCH, DIY188_INIT, DIY139_SEARCH, DIY139_INIT, CHANNEL188_SEARCH, CHANNEL188_INIT,
                CHANNEL139_SEARCH, CHANNEL139_INIT, CHANNEL137_SEARCH, CHANNEL137_INIT, ROBOT]
    
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

def parseFWDHTime(strtime):
    try:
        date = time.strptime(strtime, "%Y-%m-%d %H:%M:%S")
        d = datetime.datetime(date[0], date[1], date[2], date[3])
        return d
    except:
        print 'Error:', strtime


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
        else:
            readAppLog(f)
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
    
