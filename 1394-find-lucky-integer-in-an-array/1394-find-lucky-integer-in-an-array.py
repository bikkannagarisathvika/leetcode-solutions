class Solution:
    def findLucky(self, arr: List[int]) -> int:
        x=-1
        for i in arr:
            if arr.count(i)==i:
                x=max(x,i)
        return x

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna