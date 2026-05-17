class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        k=s.split()
        return len(k[-1])     

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna