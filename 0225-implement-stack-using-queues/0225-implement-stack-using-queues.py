class MyStack:

    def __init__(self):
        self.d1=deque()
        self.d2=deque()
    def push(self, x: int) -> None:
        while len(self.d1) > 0:
            self.d2.append(self.d1.pop())
        self.d1.append(x)
        while len(self.d2) > 0:
            self.d1.append(self.d2.pop())
    def pop(self) -> int:
        return self.d1.popleft()
    def top(self) -> int:
        return self.d1[0]
    def empty(self) -> bool:
        if len(self.d1)==0:
            return True
        else:
            return False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna