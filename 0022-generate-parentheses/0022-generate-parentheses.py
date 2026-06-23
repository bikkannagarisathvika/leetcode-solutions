class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def bt(path,open_count,close_count):
            if len(path)==2*n:
                res.append(path)
                return
            if open_count<n:
                bt(path+"(",open_count+1,close_count)
            if close_count<open_count:
                bt(path+")",open_count,close_count+1)
        bt("", 0, 0)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna