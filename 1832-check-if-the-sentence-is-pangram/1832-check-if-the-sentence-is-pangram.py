class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s=sentence.lower()
        c=0
        for i in "abcdefghijklmnopqrstuvwxyz":
            if i in s:
                c=c+1
        if c==26:
            return True
        else:
            return False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna