class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        r = [-1] * n
        s = []
        for i in range(2 * n - 1, -1, -1):
            while s and s[-1] <= nums[i % n]:
                s.pop()
            if s:
                r[i % n] = s[-1]
            s.append(nums[i % n])
        return r
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna