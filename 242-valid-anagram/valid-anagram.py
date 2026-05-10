class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        mapper = defaultdict(int)

        for x in s:
            mapper[x]+=1
        
        for i in range(len(t)):
            val = t[i]
            if val in mapper:
                if mapper[val]==1:
                    del mapper[val]
                    continue
                mapper[val]-=1
            else:
                return False
        return True
        