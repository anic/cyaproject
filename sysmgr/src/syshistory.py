# -*- coding: utf-8 -*-
import web, dao, math,sysvars

class history(sysvars.SysBase):
    
    PAGE_SIZE = 20
    
    def GET(self):
        data = web.input(ename='', page='1')
        ename = data['ename']
        
        if data['page'].isdigit():
            page = int(data['page'])
        else:
            page = 1
            
        result, pagecount = self.searchVersion(ename, page)
        return self.render().history(result, page, pagecount, ename)
    
    def searchVersion(self, ename, pageindex):
        
        db = dao.Database()
        if ename != '':
            ename = ename.strip()
            WHERE_CLAUSE = u'where c.systemename = ? '
        else:
            WHERE_CLAUSE = u''
            
        
        SQL_GETRESULT = u'select version,modifytime,modifier,systemename,s.名称,field,after from changelog as c left join systable as s on c.systemename = s.英文标识  ' + WHERE_CLAUSE + u' order by version desc'
        SQL_LEN = u'select count(*) from changelog as c ' + WHERE_CLAUSE
        
        if ename == '':
            len = db.select(SQL_LEN)
            result = db.select(SQL_GETRESULT)
            
        else:
            len = db.select(SQL_LEN, ename)
            result = db.select(SQL_GETRESULT, ename)
            
        pagesize = int(math.ceil(len[0][0] / (self.PAGE_SIZE * 1.0)))
        result = result[(pageindex - 1) * self.PAGE_SIZE: pageindex * self.PAGE_SIZE]
        return (result, pagesize)
