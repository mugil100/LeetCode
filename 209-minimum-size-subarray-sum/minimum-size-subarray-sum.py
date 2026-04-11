class Solution(object):
    def minSubArrayLen(self, target, nums):
        l=0
        res= float('inf')
        sum=0
        for r in range(len(nums)):
            sum+=nums[r]
            while sum >= target:
                res = min(r-l+1,res)
                sum-=nums[l]
                l+=1
        return res if res !=float('inf') else 0

        