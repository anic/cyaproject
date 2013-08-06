# -*- coding: utf-8 -*-
import pyodbc

global _DATABASE
class dao:
    _dbfile = ''
    def __init__(self):
        self._dbfile = _DATABASE
        pass
    
    def _cursor(self):
        conn = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb)};DBQ=' + self._dbfile)
        cursor = conn.cursor()
        return cursor
    
    def select(self, sql, *args):
        cursor = self._cursor()
        cursor.execute(sql, *args)
        rows = cursor.fetchall()
        return rows

if __name__ == '__main__':
    db = dao(u'\\\\10.244.113.83\\信息技术中心个人目录\\程曜安\\系统维护材料\\system.mdb')
    result = db.select(u'select top 10 * from systable where 名称  like ? or 英文标识 like ? or 中文别称 like ?',
                        u'%短信%', u'%短信%', u'%短信%')
    for i in result:
        print i[0], i[1], i[2]
