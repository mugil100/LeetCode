class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for x in nums:
            val = list(str(x))
            res+=(val)
        
        res=[int(y) for y in res]

        return res



        