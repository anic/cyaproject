import os, fnmatch  
  
def search(pattern, root=os.curdir):  
    for path, dirs, files in os.walk(os.path.abspath(root)):  
        for filename in fnmatch.filter(files, pattern):  
            yield os.path.join(path, filename)  
