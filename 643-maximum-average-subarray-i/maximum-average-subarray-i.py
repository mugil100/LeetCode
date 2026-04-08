class Solution(object):
    def findMaxAverage(self, nums, k):
        summ=sum(nums[0:k])
        max_sum = summ
        for j in range(k,len(nums)):
            summ+=nums[j]
            summ-=nums[j-k]
            if summ > max_sum: max_sum = summ
        return max_sum/float(k)

        