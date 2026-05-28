class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        cand= None
        for x in nums:

            if count==0:
                cand= x
                count=1
            elif x == cand:
                count+=1

            else:
                count -=1
        return cand
                


        