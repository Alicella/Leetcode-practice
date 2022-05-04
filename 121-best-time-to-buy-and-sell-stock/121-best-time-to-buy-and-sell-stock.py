class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # to maximize profit, buy at a lowest price and sell at a highest, profit = the difference
        crt_lowest = prices[0]
        max_profit = 0
        
        for p in prices[1:]:
            # crt_lowest = min(crt_lowest, p)
            # crt_highest = max(crt_highest, p)
            if p < crt_lowest:
                crt_lowest = p
            elif p > crt_lowest:
                crt_highest = p
                max_profit = max(max_profit, crt_highest - crt_lowest)      
        
        return max_profit
        