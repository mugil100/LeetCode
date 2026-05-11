class Solution:
    def isHappy(self, n: int) -> bool:
        intCount=0
        hashk = set()        
        while n!=1:
            if n in hashk:
                return False
            hashk.add(n)
            chars = str(n)
            n=0
            for x in chars:
                n += int(x)**2
        return True
            

        