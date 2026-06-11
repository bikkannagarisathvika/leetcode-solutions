class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        t=sum(nums[0:k])
        m=t
        for i in range(k,len(nums)):
            t=t+nums[i]-nums[i-k]
            m=max(m,t)
        return m/k
       

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna