# simple_copy.py -- minimalist file copying utility script.
#Author: Philip Conrad -- 8/26/2012@1:02AM
#License: New BSD License <http://opensource.org/licenses/BSD-3-Clause>

import shutil
import sys



if __name__ == '__main__':
    srcfile = sys.argv[1]
    destfile = sys.argv[2]
    if srcfile is not None:
        if destfile is not None:
            shutil.copy2(srcfile, destfile)
            print "copy complete"
