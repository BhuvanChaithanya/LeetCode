class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ""
        l,r = 0,0
        while l<len(word1) and r < len(word2):
            s = s+word1[l]
            l +=1
            s = s+ word2[r]
            r +=1

        if l < len(word1):
            s+= word1[l:]
        elif r < len(word2):
            s += word2[r:]

        return s