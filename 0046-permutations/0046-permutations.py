class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def bt(path):
            if len(path)==len(nums):
                res.append(path[:])
                return
            for i in nums:
                if i not in path:
                    path.append(i)
                    bt(path)
                    path.pop()
        bt([])
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna