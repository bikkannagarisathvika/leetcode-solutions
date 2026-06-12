class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        r=len(matrix)
        col=len(matrix[0])
        for i in range(1,r):
            for j in range(1,col):
                if matrix[i][j]!=matrix[i-1][j-1]:
                    return False
        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna