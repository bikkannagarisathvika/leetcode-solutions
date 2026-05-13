class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low=0
        high=len(numbers)-1
        while low<high:
            if target==numbers[low]+numbers[high]:
                return [low+1,high+1]
            elif target<numbers[low]+numbers[high]:
                high-=1
            else:
                low+=1
        return [-1,-1]
    
