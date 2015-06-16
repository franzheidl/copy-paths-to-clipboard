# -*- coding: utf-8 -*-

# Copy Paths to Clipboard
# Workflow For Alfred 2
# Franz Heidl 2013 - 2014
# http://github.com/franzheidl/copy-paths-to-clipboard
# MIT license.


import sys
import subprocess
from CopyAllPaths import CopyAllPaths
from AlFeedback import Feedback
from urllib import unquote

def main(q=False):

  paths = ((subprocess.check_output(['osascript', 'allpaths.applescript'])).strip()) # returns file urls string
  f_icon_name = "copypaths"

  if paths != "":
    p = CopyAllPaths(paths) #--> file ulrs array
    f_title = "Copy POSIX Paths as:"
    posixPaths = ((subprocess.check_output(['osascript', 'fileurl_to_posix.applescript', paths])).strip())
    

    if q:
      
      if "-url" in q:
          f_title = "Copy File URLs as:"
          f_icon_name += "_url"
          
      elif "-hfs" in q:
          f_title = "Copy HFS Paths as:"
          f_icon_name += "_hfs"
          paths = ((subprocess.check_output(['osascript', 'fileurl_to_hfs.applescript', paths])).strip())
          paths = unquote(paths).decode('utf-8')
          if "-q" in q:
              paths = p.quotedPaths(paths, "hfs")

      else:
          f_icon_name += "_posix"
          paths = unquote(posixPaths).decode('utf-8')
          if "-s" in q:
              paths = unquote(p.shortPaths()).decode('utf-8')
              f_icon_name += "_short"
      
      if "-q" in q:
          f_icon_name += "_quoted"
          paths = p.quotedPaths(paths)
      
      
      if "-n" in q:
          paths = p.joinNewlines(paths)
        
    else:
      f_icon_name += "_posix"
      paths = unquote(posixPaths).decode('utf-8')

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
