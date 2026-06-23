class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def bt(index,path):
            res.append(path[:])
            for i in range(index,len(nums)):
                path.append(nums[i])
                bt(i+1,path)
                path.pop()
        bt(0,[])
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna