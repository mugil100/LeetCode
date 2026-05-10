class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=[]
        f=None
        l=None
        n=len(s)
        mapper={}
        used = set()
        for i in range(n):
            if s[i]!=" ":
                if i==0 or s[i-1]==" ":
                    f=i
                if i==n-1 or s[i+1]==" ":
                    l=i
                if f is not None and l is not None:
                    words.append(s[f:l+1])
                    f=None
                    l=None
        if len(words)!= len(pattern):
            return False
        for i in range(len(pattern)):
            val = pattern[i]
            if val in mapper:
                if mapper[val]==words[i]:
                    continue
                else:
                    return False
            else:
                if words[i] in used:
                    return False
                mapper[val]=words[i]
                used.add(words[i])
        return True




        
        
        