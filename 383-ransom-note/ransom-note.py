class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = {}
        m = {}
        count=0
        for char in ransomNote:
            r[char]=r.get(char,0)+1

        for char in magazine:
            m[char]=m.get(char,0)+1

        for key,value in m.items():
            if key in r and r[key]<=value:
                count+=1
        if count==len(r):
            return True
        else:
            return False


        