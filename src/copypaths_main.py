# Copy All Paths to Clipboard
# Workflow For Alfred 2
# Franz Heidl 2013 - 2014
# MIT license.


import sys
import subprocess
from CopyAllPaths import CopyAllPaths

def main(q):
    options = []
    paths = ""

    if q:
        paths = ", ".join(q[0].split("\t"))

    if len(q) > 1:
        options = q[1:]

    p = CopyAllPaths(paths)

    if options:
        if "-hfs" in options:
            paths = ((subprocess.check_output(['osascript', 'posix_to_hfs.applescript', paths])).strip())
            if "-q" in options:
                paths = p.quotedPaths(paths, "hfs")
        else:
            if "-url" in options:
                paths = p.fileUrls()
            if "-s" in options:
                paths = p.shortPaths()
            if "-q" in options:
                paths = p.quotedPaths(paths)
            if "-p" in options:
                paths = p.posixPaths()

        if "-n" in options:
            paths = p.joinNewlines(paths)
        
    else:
        paths = p.strPaths()

    print paths

if  __name__ =="__main__":
    main(sys.argv[1:])
