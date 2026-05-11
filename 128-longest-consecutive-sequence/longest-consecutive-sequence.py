class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        n= len(nums)
        count = 1
        maxCount = 0
        
        if not nums:
            return 0

        for i in range(n-1):
            if nums[i]+1 == nums[i+1]:
                count+=1
            elif nums[i] == nums[i+1]:
                continue
            else:
                maxCount = max(maxCount,count)
                count=1

        maxCount = max(maxCount, count)

        return maxCount
        