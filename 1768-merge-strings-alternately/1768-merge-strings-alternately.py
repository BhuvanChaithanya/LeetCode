class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        sml = min(len(word1), len(word2))
        res = ""
        for i in range(sml):
            res += word1[i]
            res += word2[i]

        if len(word1)>len(word2):
            res += word1[sml:]
        else:
            res += word2[sml:]

        return res