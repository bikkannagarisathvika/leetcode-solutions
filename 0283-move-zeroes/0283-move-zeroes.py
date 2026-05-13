class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        non=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[non],nums[i]=nums[i],nums[non]
                non+=1
            