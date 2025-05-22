class Solution:
    def palindrome(self, s):
        return s==s[::-1]
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1

        while l<r:
            if s[l] != s[r]:
                return (self.palindrome(s[l+1:r+1]) or self.palindrome(s[l:r]))

            else:
                l += 1
                r -= 1

        return True