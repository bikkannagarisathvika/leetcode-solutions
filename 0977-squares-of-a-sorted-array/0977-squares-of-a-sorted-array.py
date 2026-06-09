class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res=[]
        for i in nums:
            res.append(i**2)
        res.sort()
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna