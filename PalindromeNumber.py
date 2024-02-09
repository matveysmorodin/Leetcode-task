#9. Palindrome Number
#https://leetcode.com/problems/palindrome-number/description/
#My solutions do not claim any records, chill... I'm just learning <3
class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = str(x)
        m = str(x)
        n = n[::-1]
        res = False
        if n==m:
            res = True
        if x < 0 or (n[0]=='0' and len(n)>1):
            res = False
        return res
