class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        first=0
        for second in range(1,len(nums)):
            if nums[first]!=nums[second]:
                first=first+1
                nums[first]=nums[second]
        return first+1
        