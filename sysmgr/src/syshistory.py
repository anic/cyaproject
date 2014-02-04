# -*- coding: utf-8 -*-
import web, dao, math, sysvars

class history(sysvars.SysBase):
    
    PAGE_SIZE = 20
    
    def GET(self):
        data = web.input(ename='', page='1', user='')
        ename = data['ename']
        user = data['user']
        
        if data['page'].isdigit():
            page = int(data['page'])
        else:
            page = 1
            
        result, pagecount,keyword = self.searchVersion(ename, user, page)
        return self.render().history(result, page, pagecount, keyword)
    
    def searchVersion(self, ename, user, pageindex):
        
        db = dao.Database()
        arg = ''
        if ename != '':
            arg = ename.strip()
            WHERE_CLAUSE = u'where c.systemename = ? '
        elif user != '':
            arg = user.strip()
            WHERE_CLAUSE = u'where c.modifier = ? '
        else:
            WHERE_CLAUSE = u''
            
        #限制在1000个
        MAX = 1000
        SQL_GETRESULT = u'select top {0} version,modifytime,modifier,systemename,s.名称,field,after from changelog as c left join systable as s on c.systemename = s.英文标识  ' + WHERE_CLAUSE + u' order by version desc'
        SQL_GETRESULT = SQL_GETRESULT.format(MAX) 
        SQL_LEN = u'select count(*) from changelog as c ' + WHERE_CLAUSE
        
        if arg == '':
            len = db.select(SQL_LEN)
            result = db.select(SQL_GETRESULT)
        else:
            len = db.select(SQL_LEN, ename)
            result = db.select(SQL_GETRESULT, arg)
        
        lenResult = len[0][0]
        if lenResult > MAX:
            lenResult = MAX
        
        pagesize = int(math.ceil(lenResult / (self.PAGE_SIZE * 1.0)))
        result = result[(pageindex - 1) * self.PAGE_SIZE: pageindex * self.PAGE_SIZE]
        return (result, pagesize,arg)
