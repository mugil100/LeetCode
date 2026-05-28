class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        min_p = float("inf")
        max_prof = 0
        for p in prices:
            if p < min_p:
                min_p =p
            else:
                profit = p- min_p
                if profit > max_prof:
                    max_prof = profit

        return max_prof
        

        