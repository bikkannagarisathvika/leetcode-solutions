class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x=0
        for i in operations:
            if '+' in i:
                x=x+1
            else:
                x=x-1
        return x
            

        