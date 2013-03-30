# -*- coding:utf-8 -*-

import MySQLdb, re, filesearch
import time
import datetime

def test():
    
    db = MySQLdb.connect(host="localhost", user="root", passwd="chengyaoan", db="test")
    cur = db.cursor()
    
    #execute an sql query
#    cur.execute("select * from test2")
    cur.execute('call testproc()')
    rows = cur.fetchall()
    print '---'
    for row in rows:
        print row
    
    cur = db.cursor()
    cur.execute('select * from test.aaa')
    rows = cur.fetchall()
    print '---'
    for row in rows:
        print row

    
if __name__ == '__main__':
    test()