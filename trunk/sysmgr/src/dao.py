# -*- coding: utf-8 -*-
import pyodbc

#全局数据库地址
global _DATABASE

class Database:
    _dbfile = ''
    conn = None;
    
    def __init__(self, path=None):
        if path is None:
            self._dbfile = _DATABASE
        else:
            self._dbfile = path
    
    def __del__(self):
        if self.conn:
            self.conn.close()
    
    def _cursor(self):
        if not self.conn:
            self.conn = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb)};DBQ=' + self._dbfile)
        cursor = self.conn.cursor()
        return cursor
    
    def select(self, sql, *args):
        cursor = self._cursor()
        cursor.execute(sql, *args)
        rows = cursor.fetchall()
        return rows
        
    #更新系统信息
    def updateSystemInfo(self, after, before, modifier, fields, labels, curVersion):
        print self._dbfile
        
        ename = before['ename']
        if not ename:
            return False, '传入系统名称非法'
        
        #检查系统版本号
        lastVersion = self.getSystemVersion(ename)['version']
        if lastVersion != 0 and lastVersion != curVersion:
#            print lastVersion, curVersion, lastVersion == curVersion
            return False, '当前版本({0})不是最新 ({1})，请在刷新后在最新版本上修改'.format(curVersion, lastVersion)
        
        try:
            #创建新的版本号        
            cursor = self._cursor()
            sql = 'insert into version(modifytime,modifier,systemename) values(now(),?,?)'
            cursor.execute(sql, modifier, before['ename'])
            self.conn.commit()
            
            cursor = self._cursor()
            rows = self.select('SELECT @@Identity')
            newVersion = rows[0][0]
            
            for i in range(len(fields)):
                #产生新的更新日志
                sql = u'insert into changelog(modifytime,modifier,systemename,field,before,after,version) values(now(),?,?,?,?,?,?)'
                cursor = self._cursor()
                cursor.execute(sql, modifier, ename, labels[i], before[fields[i]], after[fields[i]], newVersion)
                self.conn.commit()

                #更新当前字段            
                sql = u'update systable set ' + labels[i] + u' = ? where 英文标识 = ?'
                print sql
                print after[fields[i]], ename
                cursor = self._cursor()
                cursor.execute(sql, after[fields[i]], ename)
                self.conn.commit()
            
            return True, newVersion
            
            
        except Exception, ex:
            self.error(ex)
            return False, '更新失败'
        
    
    def error(self, ex):
        try:
            print ex[1].decode('gb2312')
        except:
            print ex
    

    #查询一个系统当前版本
    def getGlobalVersion(self):
        return self.getSystemVersion('')
    
    #查询一个系统当前版本
    def getSystemVersion(self, ename):
        if ename != '':
            sql = 'select top 1 ID as sysversion , modifytime, modifier from version where systemename = \'{0}\' order by ID desc'.format(ename)
        else:
            sql = 'select top 1 ID as sysversion , modifytime, modifier from version order by ID desc'

        rows = self.select(sql)
        if len(rows) == 0:
            #0表示未修改过
            sysversion = 0
            modifier = '-'
            modifytime = '-'
        else:
            sysversion = rows[0][0]
            modifytime = rows[0][1]
            modifier = rows[0][2]
        
        
        return {"version":sysversion,
                "modifier":modifier,
                "modifytime":modifytime}
    
    #获得列信息
    #label    name    type    editable
    #[英文标识 ,ename, common,editable]
    def getCols(self, type=None):
        if type is None:
            cols = self.select('select name, label, type, editable from dict order by display')
        else:
            cols = self.select('select name, label, type, editable from dict where type = ? order by display', type)
            
        return cols
    

if __name__ == '__main__':
    import facade
    f = facade.Facade()
    f.prepare_network(localOnly=True)
    
#    _DATABASE = u'\\\\10.244.113.83\\规划建设室\\个人目录\\业务一组\\程曜安\\system.mdb'
#    _DATABASE = u'\\\\10.244.113.83\\信息技术中心个人目录\\程曜安\\系统维护材料\\system.mdb'
#    _DATABASE = u'DRIVER={Microsoft Access Driver (*.mdb)};DBQ=f:/测试/system.mdb'
    #_DATABASE = unicode(_DATABASE,"utf-8")
#    _DATABASE = u'f:/测试/system.mdb'
#    print _DATABASE
#    db = Database()
#    result = db.select(u'select top 10 * from systable where 名称  like ? or 英文标识 like ? or 中文别称 like ?',
#                        u'%短信%', u'%短信%', u'%短信%')
#    for i in result:
#        print i[0], i[1], i[2]
#    print Database('c:/system.mdb').getSystemVersion('vsmp')
