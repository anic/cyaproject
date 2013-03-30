# -*- coding: utf-8 -*-
import pyodbc

DBfile = u'E:/work/mytask/flaws.mdb'

def _cursor():
    conn = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb)};DBQ=' + DBfile)
    cursor = conn.cursor()
    return cursor

def update_report(report):
    fileinfo, summary, details = report
    #fileinfo = (file_name, report_date, scan_date, sys_name)
    #summary = (high, medium, low, info)
    #details = [(item_id, item_title, item_degree, item_url, item_param, item_task),... ]


    conn = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb)};DBQ=' + DBfile)
    cursor = conn.cursor()

    SQL = '''insert into reportinfo(report_date,scan_date,sys_raw,filename,highflaw,mediumflaw,lowflaw,infoflaw) 
    values(?,?,?,?,?,?,?,?)'''
    #print SQL, fileinfo[1], fileinfo[2], fileinfo[3], fileinfo[0], summary[0], summary[1], summary[2], summary[3]
    try:
        cursor.execute(SQL, fileinfo[1], fileinfo[2], fileinfo[3], fileinfo[0], summary[0], summary[1], summary[2], summary[3])
        cursor.commit()
    except pyodbc.IntegrityError as e:
        print e
    
    reportid = get_report(fileinfo)
    reportname = '[' + str(fileinfo[1]) + ']' + fileinfo[0]
    update_details(conn, details, reportid, reportname)
    cursor.close()

def update_details(conn, details, reportid, reportname):
    cursor = conn.cursor()
    #details = [(item_id, item_title, item_degree, item_url, item_param, item_task),... ]
    
    SQL = '''insert into rawdata(innerid,title,degree,url,param,task,reportid,reportname) 
    values(?,?,?,?,?,?,?,?)'''
    for d in details:
        try:
            cursor.execute(SQL, d[0], d[1], d[2], d[3], d[4], d[5], reportid, reportname)
            cursor.commit()
        except pyodbc.IntegrityError as e:
            print e
            
    cursor.close()

#检查数据库一致性，删除不存在报告ID的原始数据
def check_integrity():
    print '正在检查数据库一致性...'
    cursor = _cursor()
    cursor.execute('delete from rawdata where reportid is null or reportid not in (select ID as reportid from reportinfo)')
    cursor.commit()
    cursor.close()
    
#检查漏洞数据是否未汇总漏洞信息
def has_flaw_null():
    cursor = _cursor()
    cursor.execute('select ID from rawdata where flawid is null')
    row = cursor.fetchone()
    cursor.close()
    return row is not None

def update_flaw():
    cursor = _cursor()
    cursor.execute('select d.ID,d.title,d.param,d.url,d.degree,d.task,r.sys from rawdata as d left join reportinfo as r on d.reportid = r.ID where flawid is null')
    rows = cursor.fetchall()
    for r in rows:
        rid = r[0]
        
        title = r[1]
        param = r[2]

        #统一使用http路径
        url = r[3]
        url = url.replace('https://', 'http://')
        
        degree = r[4]
        task = r[5]
        sys = r[6]
 
        #如果没有设置系统，则不处理       
        if not sys:
            continue
        
        #print title, url, param, sys

        fid = get_flaw_ID(title, url, param, sys)
        if not fid:
            create_flaw(title, url, param, sys, degree, task)
            fid = get_flaw_ID(title, url, param, sys)
            print '汇总漏洞：', fid, title, url, param, sys, degree, rid
        
        update_detail(rid, fid)
        
    return

def update_detail(rid, fid):
    cursor = _cursor()
    cursor.execute('update rawdata set flawid = ? where ID = ?', fid, rid)
    cursor.commit()
    cursor.close()

def create_flaw(title, url, param, sys, degree, task):
    cursor = _cursor()
    cursor.execute('insert into flawinfo(title,url,param,sys,degree,task) values(?,?,?,?,?,?)', title, url, param, sys, degree, task)
    cursor.commit()
    cursor.close()  

def get_flaw_ID(title, url, param, sys):
    cursor = _cursor()
    if param:
        cursor.execute('select ID from flawinfo where title = ? and sys = ? and param =? and url = ?', title, sys, param, url)
    else:
        cursor.execute('select ID from flawinfo where title = ? and sys = ? and param is null and url = ?', title, sys, url)
        
    row = cursor.fetchone()
    cursor.close()
    if row:
        return row[0]
    else:
        return None  

#检查数据库是否正常
def db_check():
    #重置ID
    if raw_input('是否删除所有数据?y/[n]') == 'y':
        reset_db()
    
    check_integrity()
    
    #检查是否有未填写的系统名称
    if has_sys_null():
        if raw_input('是否自动补充未写系统的名称？[y]/n') <> 'n':
            update_sys()
        
        if has_sys_null():
            print '[错误]存在系统名称为空，请手动补全'
            return False
    
    if has_flaw_null():
        if raw_input('是否自动汇总漏洞？[y]/n') <> 'n':
            update_flaw()
            
    return True

def get_report(fileinfo):
    cursor = _cursor()
    SQL = 'SELECT ID from reportinfo where report_date = ? and filename = ?;'
    cursor.execute(SQL, fileinfo[1], fileinfo[0])
    row = cursor.fetchone()
    cursor.close()
    if row:
        return row.ID
    else:
        return None

#补全系统名称
def update_sys():
    print '正在补全系统名称...'
    cursor = _cursor()
    cursor.execute('update reportinfo as r left join sysalias as s on r.sys_raw = s.sys_raw set r.sys = s.sys where r.sys is null and s.sys is not null')
    cursor.commit()
    cursor.close()

def has_sys_null():
    cursor = _cursor()
    cursor.execute('select ID from reportinfo where sys is null')
    row = cursor.fetchone()
    cursor.close()
    return row is not None


#重置数据库
def reset_db():
    conn = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb)};DBQ=' + DBfile)
    cursor = conn.cursor()
    cursor.execute('delete from reportinfo')
    cursor.execute('alter table reportinfo alter ID counter(1,1)')
    cursor.execute('delete from rawdata')
    cursor.execute('alter table rawdata alter ID counter(1,1)')
    cursor.execute('delete from flawinfo')
    cursor.execute('alter table flawinfo alter ID counter(1,1)')
    cursor.commit()
    cursor.close()
    
def get_flawid(title, url, param,):
    pass
