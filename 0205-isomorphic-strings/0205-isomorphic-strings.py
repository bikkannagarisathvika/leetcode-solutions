class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d={}
        for i in range(len(s)):
            if s[i] in d:
                if d[s[i]]!=t[i]:
                    return False
            else:
                if t[i] in d.values():
                    return False
                d[s[i]]=t[i]
        return True 
            


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna