class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        x=0
        r=[0]
        for i in gain:
            x=x+i
            r.append(x)
        return max(r)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna