class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hashmap = defaultdict(int)
        for i in range(n):
            hashmap[nums[i]] = i #2->0 (val to index)
        print(hashmap.items())
        for i in range(n):
            need = target - nums[i] # 9-2 =7
            if need in hashmap.keys() and hashmap[need]!=i: #element is there but not from same index
                return[i,hashmap[need]]

            