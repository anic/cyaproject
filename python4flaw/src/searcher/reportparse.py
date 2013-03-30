# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re
import os.path
from datetime import date


#用于匹配报告内容的正则模式
ID_PATTERN = re.compile(r'ID=(\d+)')
TITLE_PATTERN = re.compile(r'\[.*\]\S')
PARAM_PATTERN = re.compile(r'\((.*)\)')
SPACE_PATTERN = re.compile(r'[\s| ]') #there's a chinese space in it
DATE_PATTERN = re.compile(r'([\d]{4})\\')
SCAN_PATTERN = re.compile(r'(\d{8})\.')
SYS_PATTERN = re.compile(r'_(.*)_')
SYS_PATTERN_2 = re.compile(r'(.*)_')

#获取报告的漏洞汇总数目
def summary_report(content):
    high, medium, low, info = (0, 0, 0, 0)
    for c in content:
        if c[2] == u'高': 
            high += 1 
        elif c[2] == u'中':
            medium += 1
        elif c[2] == u'低': 
            low += 1
        else: 
            info += 1
    
    return (high, medium, low, info)

#抽取报告的基本信息
def info_report(filename):
    file_name = os.path.basename(filename)
    
    date_match = DATE_PATTERN.search(filename)
    scan_date = None
    report_date = None
    if date_match:
        report_date = date(2013, int(date_match.groups()[0][0:2]), int(date_match.groups()[0][2:4]))
    
    date_match = SCAN_PATTERN.search(file_name)
    if date_match:
        strdate = date_match.groups()[0]
        scan_date = date(int(strdate[0:4]), int(strdate[4:6]), int(strdate[6:8]))
    
    #匹配如AppScan_[系统名]_20120201.html的形式
    sys_name = None
    sys_match = SYS_PATTERN.search(file_name)
    if sys_match:
        sys_name = sys_match.groups()[0]
    else: #如果无法匹配，则匹配[系统名]_20120201.html的形式
        sys_match = SYS_PATTERN_2.search(file_name)
        if sys_match:
            sys_name = sys_match.groups()[0]
        
    #build file infomation
    return (file_name, report_date, scan_date, sys_name)


def readhtmlfile(filename):
#    f = open(filename)
#    html = ''
#    while True:
#        tmp = f.read(1024)
#        if tmp == '':
#            break
#        html += tmp
#        
#    return html
    import codecs
    html = codecs.open(filename).read()
    return html 

#分析报告
def parse_report(filename):
    print filename
    
    fileinfo = info_report(filename)
    if dao.get_report(fileinfo):
        return None #the report has been saved,no need to analyse
    
    
    #var title = document.getElementsByClassName("f34_");
    #var degree = document.getElementsByClassName("f45_");
    #var url = document.getElementsByClassName("f42_");
    #var task = document.getElementsByClassName("f69_");
    #var id = document.getElementsByClassName("f35_");
    #var d, itemid;
    #var str = "序号\tID\t标题\t严重性\tURL\t修复任务";
    #console.log(str);
    #for(var i=0,size=title.length;i<size;++i)
    #{
    #itemid = id[i].innerHTML.match(/ID=(\d+)/)[1];
    #str = i+"\t"+itemid+"\t"+title[i].innerHTML+"\t"+degree[i].innerHTML+"\t"+url[i].innerHTML+"\t"+task[i].innerHTML;
    #str = str.replace(/&nbsp;/g,"");
    #
    #console.log(str);
    #}

    result = []
    
    html = readhtmlfile(filename)
#    print html
#    print '***********'
    
    soup = BeautifulSoup(html)
    
    titles = soup.find_all('span', 'f34_')
    degrees = soup.find_all('span', 'f45_')
    urls = soup.find_all('span', 'f42_')
    ids = soup.find_all('span', 'f35_')
    tasks = soup.find_all('span', 'f69_')
    
    #TODO:f93_ f94_ f95_ 分别对应高、中、低漏洞

#    print len(tasks)
    for i in range(0, len(titles)):
        item_id = ID_PATTERN.search(ids[i].string).groups()[0]
        item_degree = degrees[i].string
        item_title = TITLE_PATTERN.sub('', titles[i].string).lstrip()
        item_url = urls[i].string.rstrip()
        
        item_param = None
        match_param = PARAM_PATTERN.search(item_url)
        if match_param:
            item_param = match_param.groups()[0]
            item_url = PARAM_PATTERN.sub('', item_url)
            item_url = SPACE_PATTERN.sub('', item_url)
            
        item_task = tasks[i].string
        record = (item_id, item_title, item_degree, item_url, item_param, item_task)
        
        if item_degree != u'参考信息':
            result.append(record)
            #print item_degree, item_id, item_title, item_url, item_param, item_task
    
    summary = summary_report(result)
    return (fileinfo, summary, result)
    
    
    
from filesearch import search
import dao 
if __name__ == '__main__':
    if not dao.db_check():
        print '数据库检查失败'
        
    else:
        files = search('*.htm*', u'E:/work/mytask/120521 漏洞扫描/flaws_target/13/')
        for f in files:
            report = parse_report(f)
            if report:
                #need to save
                dao.update_report(report)
            
    
#    parse_report(u'E:\\flaws_target\\1102\\外网\\AppScan_本地支付辅助平台后台_20121101.html')
    
    
