class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        flag=True
        for i in range (len(nums)-1):
            for j in range (i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return[i,j]
                    flag=False
                    break
            if flag==False:
                break
        if flag:
            print(-1)