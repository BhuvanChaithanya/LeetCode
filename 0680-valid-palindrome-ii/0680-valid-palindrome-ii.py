class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(l, r,s):
            while l <r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                return is_palindrome(l+1,r, s) or is_palindrome(l, r-1,s)
            l += 1
            r -=1
        return True