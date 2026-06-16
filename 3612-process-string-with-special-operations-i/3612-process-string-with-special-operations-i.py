class Solution:
    def processStr(self, s: str) -> str:
        res = []
        for ch in s:
            if ch.isalpha():
                res.append(ch)
            elif ch=='*':
                if res:
                    res.pop()
            elif ch=='#':
                res.extend(res)
            elif ch=='%':
                res.reverse()
        return "".join(res)

                




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna