class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        res = Counter(nums)
        for x in res:
            if res[x]>1:
                return True
        return False

        