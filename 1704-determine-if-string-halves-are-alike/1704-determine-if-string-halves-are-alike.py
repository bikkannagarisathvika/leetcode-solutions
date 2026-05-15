class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l = len(s)
        f = s[:l // 2]
        s = s[l // 2:]
        cf = 0
        cs = 0
        for i in f:
            if i in 'aeiouAEIOU':
                cf = cf+ 1
        for j in s:
            if j in 'aeiouAEIOU':
                cs = cs + 1
        if cf == cs:
            return True
        else:
            return False 

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna