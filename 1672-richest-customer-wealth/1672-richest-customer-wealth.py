class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        s=[]
        for i in accounts:
            s.append(sum(i))
        return max(s)
