class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d=dict()
        for i in nums:
            if i in d:
                return True
            else:
                d[i]=1
        return False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna