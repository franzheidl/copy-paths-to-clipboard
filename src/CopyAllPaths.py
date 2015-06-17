# Copy All Paths to Clipboard
# Workflow For Alfred 2
# Franz Heidl 2013 - 2014
# MIT license.

import subprocess

class CopyAllPaths:

    def __init__(self, p):
        self.urls = self.listPaths(p)
        self.paths = self.listPaths(self.posixPaths())


    def listPaths(self, p):
        return (p).split(", ")


    def strPaths(self):
        sp = ""
        for a in self.paths:
            a.strip("'")
            if sp != "":
                sp += ", "
            sp += a
        return sp
        
        
    def strUrls(self):
        su = ""
        for a in self.urls:
            a.strip("'")
            if su != "":
                su += ", "
            su += a
        return su
        
    
    def posixPaths(self):
        pp = ""
        for a in self.urls:
            p = subprocess.check_output(["osascript", "fileurl_to_posix.applescript", a]).strip()
            if pp != "":
                pp += ", "
            pp += p
        return pp


    def shortPaths(self):
        sp = ""
        for a in self.paths:
            if a.startswith("Users/"):
                a = "/" + a
            if a.startswith("/Users/"):
                a = a.split("/")[3:]
                b = "~/"
                for i in range(len(a)):
                    if i < (len(a) - 1):
                        a[i] += "/"
                    b += a[i]
                if sp != "":
                    sp += ", "
                sp += b
            else:
                if sp != "":
                    sp += ", "
                sp += a
        return sp


    def quotedPaths(self, p=False, t=False):
        if p:
            pl = self.listPaths(p)
        else:
            pl = self.paths
        qp = ""
        for p in pl:
            if t and t == "hfs":
                p = ("\"%s\"" % p)
            else:
                p = ("'%s'" % p)
            if qp != "":
                qp += ", "
            qp += p
        return qp


    def joinNewlines(self, p=False):
        if p:
            pl = self.listPaths(p)
        else:
            pl = self.paths
        np = ""
        for p in pl:
            if np != "":
                np += "\n"
            np += p
        return np
        
        
    def fileUrls(self):
        fu = ""
        for f in self.urls:
            u = subprocess.check_output(["osascript", "posix_to_fileurl.applescript", f]).strip().decode("utf-8")
            if fu != "":
                fu += ", "
            fu += u
        return fu



    def __repr__(self):
        return self.strPaths()
