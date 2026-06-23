class Solution:
    def totalNQueens(self, n: int) -> int:
        self.count=0
        cols=set()
        diag1=set()
        diag2=set()
        def bt(row):
            if row==n:
                self.count+=1
                return
            for col in range(n):
                if col in cols or (row-col) in diag1 or (row+col) in diag2:
                    continue
                cols.add(col)
                diag1.add(row-col)
                diag2.add(row+col)
                bt(row+1)
                cols.remove(col)
                diag1.remove(row-col)
                diag2.remove(row+col)
        bt(0)
        return self.count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna