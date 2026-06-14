class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=res=0
        vals ={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        while(i+1<=len(s)):
            if i+1 <len(s) and vals[s[i]] < vals[s[i+1]]:
                res+= vals[s[i+1]]-vals[s[i]]
                i+=1
            else:
                res+= vals[s[i]]
            i+=1
        return res