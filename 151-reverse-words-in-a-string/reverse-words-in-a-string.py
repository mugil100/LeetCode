class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        first= None
        last = None
        ftemp = None
        ltemp = None
        words =[]
        res=""
        for i in range(len(s)):
            if s[i]!=" ":
                if i==0 or s[i-1]== " ":
                    first = i
                    print("first ",first)
                if i== len(s)-1 or s[i+1]== " ":
                    last=i
                    words.append(s[first:last+1])
        words.reverse()
        for i in range(len(words)):
            res+=words[i]
            if i!=len(words)-1:
                res+=" "
        return res
        