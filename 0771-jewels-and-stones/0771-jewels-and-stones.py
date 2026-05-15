class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c=0
        for i in stones:
            if i in jewels:
                c=c+1
        return c

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna