class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # to maximize profit, buy at a lowest price and sell at a highest, profit = the difference
        crt_lowest = prices[0]   #setting the initial value brings huge runtime difference... why prices[0] is much slower than float('inf')?
        max_profit = 0
        
        for p in prices:
            if p < crt_lowest:
                crt_lowest = p
            
            # this one is no good, no need to make such comparison or assignments. wasting runtime
            # elif p > crt_lowest:
            #     crt_highest = p
            #     max_profit = max(max_profit, crt_highest - crt_lowest)    
                
            if p - crt_lowest > max_profit:
                max_profit = p - crt_lowest
            
        return max_profit
    
    # if the question asks the days and prices of selling/buying info:
    
#         for i, p in enumerate(prices):
#             if p <= crt_lowest:
#                 buy_day = i
#                 crt_lowest = p
#             elif p > crt_lowest:
#                 sell_day = i
#                 crt_highest = p
#                 max_profit = max(max_profit, crt_highest - crt_lowest)

#         res = {'day of buying: ': buy_day, 
#                 'buying price: ': crt_lowest,
#                 'day of selling: ': sell_day,
#                 'selling price: ': crt_highest,
#                 'profit: ': max_profit}
        