class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        t = score[:]
        score.sort(reverse=True)
        m = {}
        for i in range(len(score)):
            if i==0:
                m[score[i]]="Gold Medal"
            elif i == 1:
                m[score[i]]="Silver Medal"
            elif i == 2:
                m[score[i]]="Bronze Medal"
            else:
                m[score[i]]=str(i + 1)
        ans = []
        for x in t:
            ans.append(m[x])
        return ans
                



            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna