class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == haystack : return 0
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i: i+len(needle)]== needle:
                return i
            # for j in range(len(needle)):
            #     if haystack[i+j] != needle[j]:
            #         break
            #     if j== len(needle)-1:
            #         return i
        return -1