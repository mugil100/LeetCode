class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxlen=0
        hm = set(nums)
        for x in hm:
            if x-1 not in hm:
                y=x+1
                while y in hm:
                    y+=1
                maxlen = max(y-x,maxlen)
        return maxlen

        