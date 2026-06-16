class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stk=[]
        for i in reversed(range(len(prices))):
            x=prices[i]
            while stk and x<stk[-1]:
                stk.pop()
            if stk:
                prices[i]-=stk[-1]
            stk.append(x)
        return prices

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna