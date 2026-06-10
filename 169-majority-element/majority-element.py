class Solution(object):
    def majorityElement(self, nums):
        # keep an index for travrsign the array
        # keep an ele for markign the most repeated value
        count = 1
        cand = nums[0]

        if len(nums)<=1:
            return nums[0]

        for x in range(1,len(nums)):
            if nums[x] != cand:
                if count<1:
                    cand = nums[x]
                else:
                    count-=1
            else:
                count+=1
        return cand

                


        