class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s = set(allowed)
        count = 0
        for w in words:
            w1 = set(w)

            if w1.issubset(s):
                count += 1


        return count