class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i=1
        while i*i<=num:
            if i*i==num:
                return True
            i+=1
        return False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna