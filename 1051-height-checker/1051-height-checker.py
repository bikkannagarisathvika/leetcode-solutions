class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        n=len(heights)
        s=heights[:]
        for i in range(n-1):
            for j in range(n-i-1):
                if heights[j]>heights[j+1]:
                    heights[j],heights[j+1]=heights[j+1],heights[j]
        c=0
        for i in range(n):
            if s[i]!=heights[i]:
                c+=1
        return c

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna