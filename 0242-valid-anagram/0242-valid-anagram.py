class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1=sorted(list(s))
        l2=sorted(list(t))
        if l1==l2:
            return True
        else:
            return False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna