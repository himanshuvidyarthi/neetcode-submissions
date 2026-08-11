class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_val = max(prices)
        max_pr = 0
        j = 0
        for i in range(len(prices)): 
            if prices[i]<max_val:
                buy = prices[i]
                j = i+1
                while(j<len(prices)):
                    max_pr = max(max_pr,prices[j]-buy )
                    j +=1
        return max_pr

        