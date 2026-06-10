class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for ch in letters:
            if ch>target:
                return ch
        return letters[0]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna