class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapper = {}
        used = set()
        for i in range(len(s)):
            val = s[i]
            if val in mapper :
                if mapper[val]==t[i]:
                    continue
                else:
                    return False
            else:
                mapper[s[i]]=t[i]
                if t[i] in used:
                    return False
                used.add(t[i])
        return True
        


        