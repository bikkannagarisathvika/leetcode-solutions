class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first=0
        last=len(nums)-1
        while first<=last and nums[first]!=target:
            first+=1
        while last>=first and nums[last]!=target:
                last-=1
        if first<=last:
            return[first,last]
        return [-1,-1]



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna