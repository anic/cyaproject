# -*- coding: utf-8 -*-

from distutils.core import setup
import py2exe

setup(
      version = "0.1.0",
      description = u"抢包子助手",  
      windows=[{'script':'main.py',
               "icon_resources": [(0, "image/toast.ico")]}])
