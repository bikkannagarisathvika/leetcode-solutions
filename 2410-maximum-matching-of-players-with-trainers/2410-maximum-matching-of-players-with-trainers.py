class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        c=0
        i=0
        j=0
        while i<len(players) and j<len(trainers):
            if players[i]<=trainers[j]:
                c+=1
                i+=1
                j+=1
            else:
                j+=1
        return c

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna