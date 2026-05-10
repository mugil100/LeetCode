class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapper = defaultdict()
        used= set()
        for i in range(len(s)):
            val=s[i]
            if val  in mapper:
                if mapper[val]==t[i]:
                    continue
                else:
                    return False
            else:
                if t[i] in used:
                    return False
                mapper[val]=t[i]
                used.add(t[i])
        return True
        