class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        r=[]
        for i in range(len(sentences)):
            s=len(sentences[i].split())
            r.append(s)
        return max(r)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna