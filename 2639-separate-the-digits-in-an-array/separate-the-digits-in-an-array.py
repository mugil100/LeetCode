class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for x in nums:
            if x >9:
                val = list(str(x))
                res+=(val)
            else:
                res.append(x)
        res=[int(y) for y in res]

        return res



        