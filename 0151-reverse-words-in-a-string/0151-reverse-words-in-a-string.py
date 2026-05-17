class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([i for i in s.split(" ")[::-1] if i])

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna