class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        k = len(nums)
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[i+n])
            print(res)
        return res
        