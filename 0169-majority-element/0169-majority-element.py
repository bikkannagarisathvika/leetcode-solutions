class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d=dict()
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for (k,v) in d.items():
            if v>len(nums)//2:
                return k


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna