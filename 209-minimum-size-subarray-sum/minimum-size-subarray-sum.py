class Solution(object):
    def minSubArrayLen(self, target, nums):
        l=0
        n=len(nums)
        w=float('inf')
        sum=0
        for r in range(n):
            sum+=nums[r]
            while sum >=target :
                if r-l+1 < w: w=r-l+1
                sum-=nums[l]
                l+=1
        if w == float('inf'): return 0
        return w 
            


        