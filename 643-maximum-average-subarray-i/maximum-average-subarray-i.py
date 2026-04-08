class Solution(object):
    def findMaxAverage(self, nums, k):
        summ=0
        n=len(nums)
        for i in range(k):
            summ+=nums[i]
        max_sum = summ
        for j in range(k,n):
            summ+=nums[j]
            summ-=nums[j-k]
            if summ > max_sum: max_sum = summ
        return max_sum/float(k)

        