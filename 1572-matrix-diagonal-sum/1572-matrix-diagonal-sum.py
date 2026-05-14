class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        m=len(mat)
        s=0
        for i in range(m):
            for j in range(m):
                if i==j or i+j==m-1:
                    s=s+mat[i][j]
        return s