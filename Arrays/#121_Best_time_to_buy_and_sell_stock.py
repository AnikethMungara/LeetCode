# Time Complexity: O(n)    
# Space Complexity: O(1)=
# Using dynamic programming approach to keep track of the minimum price and maximum profit while iterating through the list of prices.


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxprofit = -inf
        minprice = inf

        for price in prices:
            if price < minprice:
                minprice = price
            elif price - minprice > maxprofit:
                maxprofit = price - minprice
        
        return maxprofit if maxprofit != -inf else 0
    




#there is another approach using two pointer technique which has the same time and space complexity.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maxprofit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxprofit = max(maxprofit, profit)
            else:
                left = right
            right += 1
        
        return maxprofit    
    