class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev=0
        temp=x
        while x>0:
            d=x%10
            rev=(rev*10)+d
            x=x//10
        if temp==rev:
            return True
        else:
            return False