__author__ = 'sjha1'

import os
paths = os.getenv('PATH') # Get the exisiting path variables

a="C:\Python27\;C:\Python27\Scripts;C:\Python27;C:\Python27\Lib\site-packages"



#Spliting paths to form a list of paths
paths_list = paths.split(";")

for path in paths_list:
    print path

