class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        hm = {}

        for i in range(len(nums)):
            hm[nums[i]] = i
        
        for i in range(len(nums)):
            need = target - nums[i]

            if need in hm.keys() and hm[need]!=i:
                return [i,hm[need]]
        return []

            