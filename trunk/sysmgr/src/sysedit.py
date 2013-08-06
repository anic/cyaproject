# -*- coding: utf-8 -*-
import web, dao

class edit:
    
    common_attr = ['ID', u'名称', u'访问方式', u'英文标识', u'中文别称', u'外网', u'子类', u'简要说明', u'上线时间', u'下线时间', u'开发商']
    common_attr_name = ['id', 'name', 'urls', 'ename', 'cname', 'web', 'clazz', 'description', 'online', 'offline', 'dev']
    
    dev_attr = ['开发_系统等级', '开发_系统名称', '开发_现状', '开发_主要使用部门', '开发_开发合作方', '开发_简易步骤', '开发_备注', '开发_系统生命周期', '开发_源代码管理']
    dev_attr_name = ['dev_level', 'dev_name', 'dev_now', 'dev_dept', 'dev_dev', 'dev_step', 'dev_comment', 'dev_lifecycle', 'dev_src']
    
    opp_attr = ['维护_系统等级', '维护_系统全称', '维护_账号管理部门', '维护_账号管理科室', '维护_支持室系统负责人', '维护_数据库备份情况', '维护_源代码完整性', '维护_已有自动业务监控点', '维护_涉及服务器', '维护_开发商联系人']
    opp_attr_name = ['opp_level', 'opp_name', 'opp_dept', 'opp_room', 'opp_oper', 'opp_backup', 'opp_src', 'opp_monitor', 'opp_server', 'opp_dever']
    
    
    
    zc_attr = []
    gh_attr = []
    
    def GET(self):
        data = web.input(en='')
        en = data['en']
        if en == '':
            web.redirect('/sys/')
            
        cvalue, dvalue, ovalue = self.getsysdetail(en)
        render = web.template.render('templates/', base='layout')
        return render.edit(cvalue, dvalue, ovalue)
    
    def POST(self):
        return

    def getsysdetail(self, ename):
        SQL = 'select ' + ','.join(self.common_attr) + ',' + ','.join(self.dev_attr) + ',' + ','.join(self.opp_attr) + u' from systable where 英文标识  = ?'
        db = dao.dao()
        result = db.select(SQL, ename)
        
        if len(result) > 0:
#            for i in range(len(self.common_attr)):
#                print self.common_attr[i], result[0][i]
            
            return self.wrap_cvalue(result[0])
        else:
            return None
        
    def wrap_cvalue(self, sqlresult):
        
        common = {}
        common_len = len(self.common_attr)
        for i in range(common_len):
            common[self.common_attr_name[i]] = sqlresult[i]
             
        common['id'] = int(sqlresult[0])
        

        dev = {}
        dev_len = len(self.dev_attr)
        for i in range(dev_len):
            dev[self.dev_attr_name[i]] = sqlresult[i + common_len]
        
        opp = {}
        opp_len = len(self.opp_attr)
        for i in range(opp_len):
            dev[self.opp_attr_name[i]] = sqlresult[i + common_len + dev_len]
        
        return common, dev, opp

if __name__ == "__main__":
    edit().getsysdetail('ercp')
