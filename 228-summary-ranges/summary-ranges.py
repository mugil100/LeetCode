class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        hm=set(nums)
        res = []
        last = None
        for i in range(len(nums)):
            if nums[i]-1 not in hm:
                first=nums[i]
                k=i
                while nums[k]+1 in hm:
                    last = nums[k]+1
                    k+=1
                if last is not None:
                    res.append(str(first)+"->"+str(last))
                    last = None
                else:
                    res.append(str(first))
        print(res)
        return res
                

        