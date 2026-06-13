class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i=='+':
                a=stack.pop()
                b=stack.pop()
                stack.append(b+a)
            elif i=='-':
                a=stack.pop()
                b=stack.pop()
                stack.append(b-a)
            elif i=='*':
                a=stack.pop()
                b=stack.pop()
                stack.append(b*a)
            elif i=='/':
                a=stack.pop()
                b=stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(i))
        return stack.pop()

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna