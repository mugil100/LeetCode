class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums) 
    
        if nums[-1] >= len(nums):
            return False
        for i in range(n):
            if i==n-1:
                if nums[i]==n-1:
                    return True
            if nums[i]!=i+1:
                return False
        