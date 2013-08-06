# -*- coding: utf-8 -*-
import web, dao, math, string

class search:
    PAGE_SIZE = 10
    WHERE_CLAUSE = 'where 名称  like ? or 英文标识 like ? or 中文别称 like ?'
    SQL_LEN = u'select count(*) from systable '
    SQL_GETRESULT = u'select ID,名称,英文标识,访问方式,维护_系统等级,开发_系统等级 from systable '
    
    def GET(self):
        data = web.input(keyword=None, page='1')
        keyword = data['keyword']
        if data['page'].isdigit():
            page = int(data['page'])
        else:
            page = 1
        result, pagesize = self.search_sys(keyword, page)
        render = web.template.render('templates/', base='layout')
        return render.search(result, page, pagesize, keyword)
    
    def search_sys(self, keyword, pageindex):
        db = dao.dao()
        if keyword is not None:
            keyword = string.strip(keyword)
        
        if keyword is None or keyword == '':
            
            len = db.select(self.SQL_LEN)
            result = db.select(self.SQL_GETRESULT)
        else:
            wrap = '%' + keyword + '%'
            len = db.select(self.SQL_LEN + self.WHERE_CLAUSE, wrap, wrap, wrap)
            result = db.select(self.SQL_GETRESULT + self.WHERE_CLAUSE, wrap, wrap, wrap)
            
            
        pagesize = int(math.ceil(len[0][0] / (self.PAGE_SIZE * 1.0)))
        result = result[(pageindex - 1) * self.PAGE_SIZE: pageindex * self.PAGE_SIZE]
        return (result, pagesize)