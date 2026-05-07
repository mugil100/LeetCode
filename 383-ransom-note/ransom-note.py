class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = {}
        count=0
        for char in ransomNote:
            if char in r:
                r[char]+=1
            else:
                r[char]=1
        m = {}
        for char in magazine:
            if char in m:
                m[char]+=1
            else:
                m[char]=1
        for key,value in m.items():
            if key in r and r[key]<=value:
                count+=1
        if count==len(r):
            return True
        else:
            return False


        