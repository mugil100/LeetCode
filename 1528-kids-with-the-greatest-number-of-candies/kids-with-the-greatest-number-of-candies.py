class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCand = max(candies)
        res = []
        for x in candies:
            if x + extraCandies >= maxCand:
                res.append(True)
            else:
                res.append(False)
        return res

        