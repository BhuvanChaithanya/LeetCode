class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        res = 0
        for v, c in count.items():
            if c%2 ==0:
                res += c

        if res < len(s):
            return res+1

        else:
            return res