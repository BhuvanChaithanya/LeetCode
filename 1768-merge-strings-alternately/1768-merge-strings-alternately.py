class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = len(word1)
        r = len(word2)
        merged = []
        k = 0
        while k < min(l,r):
            merged.append(word1[k])
            merged.append(word2[k])
            k += 1
            

        while k < l:
            merged.append(word1[k])
            k += 1
        while k < r:
            merged.append(word2[k])
            k += 1
        return "".join(merged)