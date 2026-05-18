class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = set()
        buy = 0
        for sell in range(len(prices)):
            if prices[sell] < prices[buy] and prices[buy] > prices[sell]: 
                buy = sell
            else: 
                profit.add(prices[sell] - prices[buy])
        if not profit: 
            return 0
        else: 
            return max(profit)
        # low=0
        # high=1
        # Mprofit=0
        
        # while high<len(prices):
        #     if prices[high]>prices[low]:
        #         profit=prices[high]-prices[low]
        #         Mprofit=max(Mprofit,profit)
        #     else:
        #         high=low
        #     low+=1
        # return Mprofit