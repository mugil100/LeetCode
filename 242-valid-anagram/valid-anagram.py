class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        mapper = defaultdict(int)
        for x in s:
            mapper[x]+=1  
        for x in t:
            if x not in mapper or mapper[x]==0:
                return False
            mapper[x]-=1
        return True
        