# Copy Paths to Clipboard
# Workflow For Alfred 2
# Franz Heidl 2013
# http://github.com/franzheidl/copy-paths-to-clipboard
# MIT license.


import sys
import subprocess
from CopyPaths import CopyPaths

def main(q):
    options = []
    paths = ""
    
    if q:
        paths = ", ".join(q[0].split("\t"))
    
    if len(q) > 1:
        options = q[1:]
    
    p = CopyPaths(paths)
     
    if options:
        if "hfs" in options:
            paths = ((subprocess.check_output(['osascript', 'posix_to_hfs.applescript', paths])).strip())
            if "-q" in options:
                paths = p.quotedPaths(paths, "hfs")
        else:
            if "-s" in options:
                paths = p.shortPaths()
            if "-q" in options:
                paths = p.quotedPaths(paths)
        if "-n" in options:
            paths = p.joinNewlines(paths)
    else:
        paths = p.strPaths()
            
    print paths

if  __name__ =="__main__":
    main(sys.argv[1:])
        