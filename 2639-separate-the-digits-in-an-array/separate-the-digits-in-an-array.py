class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for x in nums:
            for char in str(x):
                res.append(int(char))
        return res



        