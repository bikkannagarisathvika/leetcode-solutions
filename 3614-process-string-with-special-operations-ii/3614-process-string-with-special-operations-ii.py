class Solution:
    def processStr(self, s: str, k: int) -> str:
        m = 0
        for c in s:
            if c.isalpha():
                m+=1
            elif c=='*':
                m=max(0,m-1)
            elif c=='#':
                m*=2
            elif c=='%':
                pass
        if k>=m:
            return '.'
        for c in reversed(s):
            if c=='*':
                m+=1
            elif c=='#':
                m//=2
                if k>=m:
                    k-=m
            elif c=='%':
                k=m-1-k
            else:
                m-=1
                if k==m:
                    return c


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna