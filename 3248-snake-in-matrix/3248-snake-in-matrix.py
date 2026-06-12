class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        i,j=0,0
        for c in commands:
            if c=="RIGHT":
                j+=1
            elif c=="LEFT":
                j-=1
            elif c=="DOWN":
                i+=1
            elif c=="UP":
                i-=1
        return (i*n)+j


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna