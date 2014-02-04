# -*- coding: utf-8 -*-
import web
import syssearch, sysedit, syshistory, sysvars, sysabout

class StaticFile():
    def GET(self, file):
        web.seeother('/static/' + file); #重定向  

class SysmgrApp(web.application):
    
    def run(self, port=8080, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0', port))

    def GET(self):
        web.redirect('/sys/')
    
urls = (
        '/', 'SysmgrApp',
        
        '/(.*.ico)', StaticFile, #处理ico文件  
        '/(.*.html)', StaticFile,
        '/(.*.js)', StaticFile,
        '/(.*.css)', StaticFile,
        
        '/sys/', syssearch.search,
        '/sys/edit', sysedit.edit,
        '/sys/history', syshistory.history,
        '/sys/about', sysabout.about
        )
        
if __name__ == "__main__":
    
    import facade
    f = facade.Facade()
    f.prepare_network()
    
    sysvars._LOGIN_USER = 'chengyaoan'
    sysvars._EDITABLE = True
    sysvars._MODE = "remote"
    
    app = SysmgrApp(urls, globals())
    app.run(port=f.port)

