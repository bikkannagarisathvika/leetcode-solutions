class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        for i in range(len(nums)):
            if i > reach:
                return False
            reach = max(reach, i + nums[i])
        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna