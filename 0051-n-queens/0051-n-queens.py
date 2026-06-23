class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        cols=set()
        diag1=set()
        diag2=set()
        board=[["."]*n for _ in range(n)]
        def bt(row):
            if row==n:
                res.append(["".join(r) for r in board])
                return
            for col in range(n):
                if (col in cols) or (row-col in diag1) or (row+col in diag2):
                    continue
                cols.add(col)
                diag1.add(row-col)
                diag2.add(row+col)
                board[row][col]="Q"
                bt(row+1)
                board[row][col]="."
                cols.remove(col)
                diag1.remove(row-col)
                diag2.remove(row+col)
        bt(0)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna