# -*- coding:utf-8 -*-

import re, filesearch
import time
import datetime

def output_result(date, counts):
    f = open('4g_analyse.txt', 'a')
    f.write('{0}\t{1}\t{2}\t{3}\n'.format(date, counts[0], counts[1], counts[2]))



        
        
def readAccessLog(filename):
    PATTERN_INDEX = re.compile(r"/gzdh/map4G.jsp")
    PATTERN_MAP = re.compile(r"/gzdh/map4G2.jsp")
    PATTERN_SEARCH = re.compile(r"/gzdh/client/recruit/openMapList.do")
    
    patterns = [PATTERN_INDEX, PATTERN_MAP, PATTERN_SEARCH]
    counts = [0, 0, 0]
    
    
    filereg = re.compile(r'\d{4}-\d{2}-\d{2}')
    fs = filereg.findall(filename)
    
    if not fs is None:
        date = time.strptime(fs[0], "%Y-%m-%d")
    
    linecount = 0
    
    for line in open(filename):
        #211.139.145.139 - - [30/Sep/2012:03:41:25 +0800] "GET /gzdh/client/snPhone/searchBeautifulNumber.do HTTP/1.1" 200 5739
        aline = line.strip()
        linecount += 1
        if linecount % 1000 == 0:
            print 'line count:', linecount
        
        for i in range(0, len(patterns)):
            m = patterns[i].search(aline)
            if m is not None:
                counts[i] = counts[i] + 1
                break
    
    output_result(time.strftime('%Y-%m-%d', date), counts)


if __name__ == '__main__':
    
#    output_result('2012-01-03', [0, 1, 2])
    
    FILE_TYPE_ACCESSLOG = re.compile(r'localhost_access_log')
    FILE_TYPE_FWDHLOG = re.compile(r'fwdh_logs')
    
    files = filesearch.search("*", 'F:/fwdh_logs/')
    for f in files:
        if FILE_TYPE_ACCESSLOG.search(f) is not None:
            readAccessLog(f)
