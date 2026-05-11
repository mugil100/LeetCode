class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        hashk = {}
        for i in range(n):
            if nums[i] in hashk and abs(i-hashk[nums[i]])<=k:
                return True
            hashk[nums[i]]=i
        return False
        