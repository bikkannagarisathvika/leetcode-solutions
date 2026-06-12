class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        d=dict()
        for i in nums:
            d[i]=1
        for i in range(len(nums)+1):
            if i not in d:
                return i

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna