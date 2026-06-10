class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        row_mins = []
        for row in matrix:
            row_mins.append(min(row))
        rows = len(matrix)
        cols = len(matrix[0])
        luckies = []
        for j in range(0,cols):
            col = []
            for i in range(0,rows):
                col.append(matrix[i][j])
            if max(col) in row_mins:
                luckies.append(max(col))
        return luckies
    

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna