class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left=0
        right=len(arr)-1
        while left<=right:
            mid=(left+right)//2
            miss=arr[mid]-(mid+1)
            if miss<k:
                left=mid+1
            else:
                right=mid-1
        return k+left

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna