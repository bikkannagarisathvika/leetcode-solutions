class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        c=0
        m=0
        for i in range(len(nums)):
            if nums[i]==0:
                c+=1
            while c>k:
                if nums[l]==0:
                    c-=1
                l+=1
            m=max(m,i-l+1)
        return m

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna