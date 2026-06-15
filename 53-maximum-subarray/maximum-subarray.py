class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        sum = max_sum = nums[0]
        for i in range(1,n):
            sum = max(sum,0)+ nums[i]
            max_sum = sum if sum>max_sum else max_sum
        return max_sum        
