class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words= s.split()
        f=None
        l=None
        n=len(s)
        mapper={}
        used = set()
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




        
        
        