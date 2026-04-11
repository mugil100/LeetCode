class Solution(object):
    def minSubArrayLen(self, target, nums):
        l=0
        res= float('inf')
        n=len(nums)
        sum=0
        for r in range(n):
            sum+=nums[r]
            while sum >= target:
                res = min(r-l+1,res)
                sum-=nums[l]
                l+=1
                if res ==1: return 1
        if res== float('inf'): return 0
        return res

        