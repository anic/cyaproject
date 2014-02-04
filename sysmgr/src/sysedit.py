# -*- coding: utf-8 -*-
import web, dao, json, sysvars 

class edit(sysvars.SysBase):
    
    
    def GET(self):
        data = web.input(ename='', tip='')
        
        ename = data['ename']
        if ename == '':
            web.redirect('/sys/')
            return
        
        #是否显示提示
        tip = data['tip']
        if tip == '':
            showtip = 'none'
            backurl = 'javascript:history.back()'
        else:
            showtip = 'block'
            backurl = '/'
        
        #获得系统信息            
        sysinfo = self.getsysdetail(ename)
        #获得系统最新版本信息
        version = dao.Database().getSystemVersion(ename) 
        return self.render().edit(sysinfo, version, showtip, backurl)
    
    def POST(self):
        data = web.input(ename='', action='')
        action = data.action
        ename = data.ename
        
        
            
        
        #处理预提交
        if action == 'presubmit':
            result = {'code':0, 'msg':'', 'field':[], 'label':[]}
            #file:///D:/Program/Reference/twitter-bootstrap/docs/components.html

            if not self.isEditable():
                result['code'] = 1
                result['msg'] = '数据库无法修改（可能由于离线、匿名登录或数据库不可写）'
            elif ename == '':
                result['code'] = 1
                result['msg'] = '格式错误'
            else:
                result['code'] = 0

                after = data
                before = self.getsysdetail(ename)
                result['field'], result['label'] = self.diffInfo(before, after)
                if len(result['field']) == 0:
                    result['msg'] = '系统信息未修改，无需保存'
                else:    
                    result['msg'] = '确认修改以下内容：'
                    
                
            web.header('Content-Type', 'application/json')
            return json.dumps(result)
        elif action == 'save':
            if ename == '':
                return self.render().error('操作失败失败')
            elif not self.isEditable(): #检查是否可写
                return self.render().error('数据库无法修改（可能由于离线、匿名登录或数据库不可写）')
            
            after = data
            before = self.getsysdetail(ename)
            fields, labels = self.diffInfo(before, after)
            if len(fields) == 0:
                return self.render().error('没有需要修改的内容')
            
            curVersion = int(data['sys_version'])
            result, msg = dao.Database().updateSystemInfo(after, before, self.loginUser(), fields, labels, curVersion)
            
            if result:
                web.redirect('/sys/edit?ename=' + ename + '&tip=savesuccess')
                return
            else:
                return self.render().error(msg)
                
                
    #比较差异
    def diffInfo(self, before, after):
        db = dao.Database()
        cols = db.getCols()
        #获取不需要保存的字段
        unchange = []
        for col in cols:
            #editable
            if col[3] == 0:
                unchange.append(col[0])
        
        result = []
        
        for attr in before:
            #不可修改的属性跳过
            if attr in unchange:
                continue
            #比较是否有变化
            if not self.testEqual(before[attr], after[attr]):
#                print attr
#                print before[attr]
#                print after[attr]
                result.append(attr)
        
        #保持result与label的对应
        label = []
        for r in result:
            for c in cols:
                if c[0] == r:
                    label.append(c[1])
                    break
                    
        return result, label
    
    def testEqual(self, beforeValue, afterValue):
        #需要处理以下情况
        #对于None和空字符
        #对于回车
        if beforeValue is None and afterValue == '':
            return True
        elif beforeValue is not None:
            #在数据库中的内容，需要替换\n ，在网页中的内容需要替换\r\n
            adjustBefore = beforeValue.replace('\n', '').replace('\r\n', '').strip()
            adjustAfter = afterValue.replace('\r\n', '').strip()
            if adjustBefore == adjustAfter:
                return True
        
        return  beforeValue == afterValue

    def getsysdetail(self, ename):
        db = dao.Database()
        cols = db.getCols()
        attr_str = ','.join([r[1] for r in cols])
        
        sql = 'select ' + attr_str + u' from systable where 英文标识  = ?'
        result = db.select(sql, ename)
        
        if len(result) > 0:
            return self.wrap_cvalue(result[0], cols)
        else:
            return None
        
    def wrap_cvalue(self, row, cols):
        
        result = {}
#        common = {}
#        dev = {}
#        opp = {}
        for i in range(len(cols)):
            type = cols[i][2]
            name = cols[i][0]
            label = cols[i][1]
            #特殊处理
            if label == 'ID':
                result[name] = int(row[i])
            else:
                result[name] = row[i]
        
        return result

if __name__ == "__main__":
    edit().getsysdetail('ercp')
