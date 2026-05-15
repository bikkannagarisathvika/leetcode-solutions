class Solution:
    def reverseWords(self, s: str) -> str:
        word=s.split()
        for i in range(len(word)):
            word[i]=word[i][::-1]
        return " ".join(word)
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna