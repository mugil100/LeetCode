class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        check = defaultdict(int)
        for char in magazine:
            check[char]+=1
        
        for c in ransomNote:
            if c not in check:
                return False
            elif check[c]==1:
                del check[c]
            else:
                check[c]-=1
        return True
        


        