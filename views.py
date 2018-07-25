import sys
sys.path.append('controllers')

'''
Add your pages down here as imported modules from the /controllers directory. Each
page should have an import statement. This is how we are connecting our controllers 
to our website!

For example, if your page is named file.py, write:
	from file import *
'''

from index import *
from schools import *
from subjects import *
from catalog_num import *
from course_descrip import *
from sections import *
from backpack import *