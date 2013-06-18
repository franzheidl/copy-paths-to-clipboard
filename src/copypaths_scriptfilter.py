# -*- coding: utf-8 -*-

# Copy Paths to Clipboard
# Workflow For Alfred 2
# Franz Heidl 2013
# http://github.com/franzheidl/copy-paths-to-clipboard
# MIT license.


import sys
import subprocess
from CopyPaths import CopyPaths
from AlFeedback import Feedback

def main(q=False):
    
    paths = ((subprocess.check_output(['osascript', 'path_target_posix.applescript'])).strip()).decode("utf-8")
    f_icon_name = "copypaths"
    
    if paths != "":
        p = CopyPaths(paths)
        f_title = "Copy POSIX Path as:"
        
        if q:
            if "hfs" in q:
                f_title = "Copy HFS Path as:"
                f_icon_name += "_hfs"
                paths = ((subprocess.check_output(['osascript', 'posix_to_hfs.applescript', paths])).strip()).decode("utf-8")
                if "-q" in q:
                    f_icon_name += "_quoted"
                    paths = p.quotedPaths(paths, "hfs")
            else:
                f_icon_name += "_posix"
                if "-s" in q:
                    paths = p.shortPaths()
                    f_icon_name += "_short"
                if "-q" in q:
                    f_icon_name += "_quoted"
                    paths = p.quotedPaths(paths)
            if "-n" in q:
                paths = p.joinNewlines(paths)
        else:
            f_icon_name += "_posix"
            paths = p.strPaths()
        f_sub = paths
        f_valid = "yes"
        
    else:
        f_icon_name += "_error"
        f_title = "Copy Paths:"
        f_sub = "Couldn't get any path"
        f_valid = "no"
    f_icon = f_icon_name + ".png"
    
    feedback = Feedback()
    feedback.addItem(title=f_title, subtitle=f_sub, valid=f_valid, arg=paths, icon=f_icon)
    print feedback

if  __name__ =="__main__":
    main(sys.argv[1:])
    