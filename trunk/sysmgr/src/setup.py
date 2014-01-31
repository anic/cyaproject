# -*- coding: utf-8 -*-

from distutils.core import setup
import py2exe
import os
import glob

#只能处理单层的查找
def find_data_files(source, target, patterns):
    """Locates the specified data-files and returns the matches
    in a data_files compatible format.

    source is the root of the source data tree.
        Use '' or '.' for current directory.
    target is the root of the target data tree.
        Use '' or '.' for the distribution directory.
    patterns is a sequence of glob-patterns for the
        files you want to copy.
    """
    if glob.has_magic(source) or glob.has_magic(target):
        raise ValueError("Magic not allowed in src, target")
    ret = {}
    for pattern in patterns:
        pattern = os.path.join(source, pattern)
        for filename in glob.glob(pattern):
            if os.path.isfile(filename):
                targetpath = os.path.join(target, os.path.relpath(filename, source))
                path = os.path.dirname(targetpath)
                ret.setdefault(path, []).append(filename)
    return sorted(ret.items())

if __name__ == '__main__':
    #需要配置拷贝的资源，下列方法无法递归创建目录，所以要手动创建
    data_files = [('', ['system.ini', 'config.ini', 'system.mdb'])]
    data_files = data_files + [("static/css", glob.glob("static/css/*"))]
    data_files = data_files + [("static/img", glob.glob("static/img/*"))]
    data_files = data_files + [("static/js", glob.glob("static/js/*.js"))]
    data_files = data_files + [("static/js/google-code-prettify", glob.glob("static/js/google-code-prettify/*"))]
    
#    resource = find_data_files("static/css", "static/css", '*')
#    exit()
    setup(
           options={
                "py2exe":{
                "dll_excludes": ["MSVCP90.dll", "HID.DLL", "w9xpopen.exe"]
            }},
          version="0.1.0",
          description=u"系统信息维护助手",
          windows=[{'script':'main.py'}],
          data_files=data_files
          )
#              (r'mpl-data\images',glob.glob(r'C:\Python25\Lib\site-packages\matplotlib\mpl-data\images\*.*')),
