class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        n = len(prices)
        profit = 0
        effBuyPrice = prices[0]

        for i in range(1,n):
            profit = max(profit, prices[i] - effBuyPrice - fee)
            effBuyPrice = min(effBuyPrice, prices[i] - profit)
        
        return profit
