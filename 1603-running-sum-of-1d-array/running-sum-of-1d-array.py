class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        init = 0
        for i in range(len(nums)):
            init+=nums[i]
            nums[i]=init
        return nums
            
        