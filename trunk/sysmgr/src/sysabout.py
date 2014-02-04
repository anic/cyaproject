# -*- coding: utf-8 -*-
import web, dao, json, sysvars 

class about(sysvars.SysBase):
    
    def GET(self):
        return self.render().about(None)
