# -*- coding: utf-8 -*-

from distutils.core import setup
import py2exe

setup(
      windows=[{'script':'main.py',
               "icon_resources": [(0, "image/toast.ico")]}])
