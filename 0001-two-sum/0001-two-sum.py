class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i,k in enumerate(nums):
            if target-k in d:
                return [d[target-k],i]
            d[k]=i

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna