class Solution:
    def simplifyPath(self, path: str) -> str:
        dir = path.split("/")
        simple = []
        for p in dir:
            if p == "" or p == ".":
                continue
            elif p == "..":
                if len(simple) > 0:
                    simple.pop()
            else:
                simple.append(p)
        
        finalPath = "/".join(simple)
        #if len(simple) == 1:
         #   finalPath += "/"
        return "/" + finalPath
            