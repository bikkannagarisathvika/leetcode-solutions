class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        left = 0
        maxf = 0
        ans = 0
        for right in range(len(s)):
            idx = ord(s[right]) - ord('A')
            count[idx] += 1
            maxf = max(maxf, count[idx])
            while (right - left + 1) - maxf > k:
                count[ord(s[left]) - ord('A')] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna