class Solution:
    def replaceDigits(self, s: str) -> str:
        r=""
        for i in range(len(s)):
            if i%2==0:
                r+=s[i]
            else:
                r+=chr(ord(s[i-1])+int(s[i]))
        return r

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna