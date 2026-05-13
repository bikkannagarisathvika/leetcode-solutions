class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        x=0
        r=[0]
        for i in gain:
            x=x+i
            r.append(x)
        return max(r)