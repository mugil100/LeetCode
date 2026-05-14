class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        filePath = path.split("/")
        
        for x in filePath:
            if x != "":
                if x==".":
                    continue
                elif x=="..":
                    if stack:
                        stack.pop()
                else:
                    stack.append(x)
        return "/"+"/".join(stack)



        