from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        if t == "": return ""
        if len(t) > len(s): return ""

        window = {} # window for checking
        countT = Counter(t) # counter hashmap for checking
        have, need = 0, len(countT) # have, required count
        l=0
        res, resLen = [-1,-1], float("infinity")
        for r in range(len(s)):
            c = s[r]
            window[c] = 1+window.get(c,0)

            if c  in countT and window[c] == countT[c]:
                have+=1
            while have == need:
                if (r-l+1) < resLen:
                    res=[l,r]
                    resLen = r-l+1
                #pop from the left of the window
                window[s[l]]-=1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have-=1
                l+=1
        l,r = res
        return s[l:r+1] if resLen != float("infinity") else ""

        
        