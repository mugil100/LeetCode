class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l=0
        hashSet=set()
        w=0
        for r in range(len(s)):
            while s[r] in hashSet:
                hashSet.remove(s[l])
                l+=1
            w = r-l+1 if r-l+1 > w else w
            hashSet.add(s[r])
        return w

        