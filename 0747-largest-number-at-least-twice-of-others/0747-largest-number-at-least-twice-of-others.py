class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m=max(nums)
        i=nums.index(m)
        for n in nums:
            if n!=m and m<2*n:
                return -1
        return i


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna