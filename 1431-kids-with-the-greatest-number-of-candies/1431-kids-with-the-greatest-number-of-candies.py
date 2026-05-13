class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        r=[]
        maximum=max(candies)
        for i in candies:
            if i+extraCandies>=maximum:
                r.append(True)
            else:
                r.append(False)
        return r
