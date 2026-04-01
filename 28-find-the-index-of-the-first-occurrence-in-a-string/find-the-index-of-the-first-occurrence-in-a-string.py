class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        first = needle[0]
        if len(needle)> len(haystack):  return -1
        for i in range(len(haystack)):
            if haystack[i]==first:
                if len(needle)== 1: return i
                x=i+1
                for j in range(1,len(needle)):
                    if x>=len(haystack) or needle[j]!=haystack[x]:  
                        break
                    if j== len(needle)-1:
                        return i  
                    x+=1          
        return -1

            
        