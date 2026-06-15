class MyStack:

    def __init__(self):
        self.s=[]
    def push(self, x: int) -> None:
        self.s.append(x)
    def pop(self) -> int:
        return self.s.pop()
    def top(self) -> int:
        return self.s[-1]
    def empty(self) -> bool:
        if len(self.s)==0:
            return True
        else:
            return False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna