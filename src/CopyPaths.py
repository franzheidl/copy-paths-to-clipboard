# Copy Paths to Clipboard
# Workflow For Alfred 2
# Franz Heidl 2013
# http://github.com/franzheidl/copy-paths-to-clipboard
# MIT license.


class CopyPaths:
    
    def __init__(self, p):
        self.paths = self.listPaths(p)
        
    
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
        


    def __repr__(self):
        return self.strPaths()
        