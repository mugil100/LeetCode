class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell =1
        maxP = 0

        while sell < len(prices):
            if prices[sell]>prices[buy]:
                maxP += prices[sell] - prices[buy]
            buy+=1
            sell+=1
        return maxP



        