class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        s=prices[0]+prices[1]
        if s<=money:
            return money-s
        else:
            return money

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna