class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=0
        sett= set()
        maxW=0
        w =0
        for r in range(len(s)):
            while s[r] in sett:
                sett.remove(s[l])
                l+=1
                
            sett.add(s[r])
            w = r-l+1
            maxW = max(w, maxW)
        return maxW


        