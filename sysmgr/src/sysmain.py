# -*- coding: utf-8 -*-
import web
import connector, configer, dao, syssearch, sysedit

urls = ('/', 'sysmgrapp',
        '/sys/', syssearch.search,
        '/sys/edit', sysedit.edit
        )

class sysmgrapp(web.application):
    def run(self, port=8080, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0', port))

    def GET(self):
        web.redirect('/sys/')
        
if __name__ == "__main__":
    
    conn = connector.fsconnection()
    cf = configer.instance().param
    
    #在内网环境
#    if conn.check_netuse(cf['remotepath'], 'GZIAP\\' + cf['username'], cf['password']):
#        print u'无法连接目标'
#        mydatabase = cf['remotepath'] + "\\" + cf['location'].decode('gbk').encode('utf-8')
#    else:
#        mydatabase = cf['localpath']
    mydatabase = cf['localpath']
    
    dao._DATABASE = mydatabase
    myport = conn.check_port()
    cf['port'] = myport
    
    app = sysmgrapp(urls, globals())
    app.run(port=myport)

