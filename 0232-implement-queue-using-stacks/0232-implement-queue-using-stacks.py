class MyQueue:

    def __init__(self):
        self.s=[]
    def push(self, x: int) -> None:
        self.s.append(x)
    def pop(self) -> int:
        return self.s.pop(0)
    def peek(self) -> int:
        return self.s[0]
    def empty(self) -> bool:
        if len(self.s)==0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna