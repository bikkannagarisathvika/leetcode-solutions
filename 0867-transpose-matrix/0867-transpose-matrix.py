class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m=len(matrix)
        n=len(matrix[0])
        a=[]
        for i in range(n):
            r=[]
            for j in range(m):
                r.append(matrix[j][i])
            a.append(r)
        return a
        