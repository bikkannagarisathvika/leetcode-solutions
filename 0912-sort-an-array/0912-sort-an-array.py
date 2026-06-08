class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergesort(nums):
            if len(nums)>1:
                left=nums[:len(nums)//2]
                right=nums[len(nums)//2:]
                mergesort(left)
                mergesort(right)
                i=j=k=0
                while i<len(left) and j<len(right):
                    if left[i]<right[j]:
                        nums[k]=left[i]
                        i+=1
                        k+=1
                    else:
                        nums[k]=right[j]
                        j+=1
                        k+=1
                while i<len(left):
                    nums[k]=left[i]
                    i+=1
                    k+=1
                while j<len(right):
                    nums[k]=right[j]
                    j+=1
                    k+=1
        mergesort(nums)
        return nums

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna