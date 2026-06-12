class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=prices[0]
        profit=0
        for i in prices:
            m=min(m,i)
            p=i-m
            profit=max(profit,p)
        return profit

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna