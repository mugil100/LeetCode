class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        res=set()
        for i in range(len(nums)):
            j=i+1
            k= len(nums)-1
            while j<k:
                if nums[i] + nums[j] + nums[k] == 0:
                    res.add(tuple([nums[i] , nums[j] , nums[k]]))
                    j+=1
                    k-=1
                elif nums[i] + nums[j] + nums[k] >0:
                    k-=1
                else:
                    j+=1
        return list(res)

