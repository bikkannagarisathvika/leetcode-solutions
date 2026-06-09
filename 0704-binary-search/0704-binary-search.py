class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if target==nums[i]:
                return i
        else:
            return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna