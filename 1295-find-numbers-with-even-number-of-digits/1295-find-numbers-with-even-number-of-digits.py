class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c=0
        for i in nums:
            res=int(math.log10(i))+1
            if res%2==0:
                c=c+1
        return c
