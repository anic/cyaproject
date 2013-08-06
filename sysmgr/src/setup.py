# -*- coding: utf-8 -*-

from distutils.core import setup
import py2exe

setup(
      version = "0.1.0",
      description = u"系统信息维护助手",
      windows=[{'script':'main.py'}])
