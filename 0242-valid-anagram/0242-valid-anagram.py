class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmapS = {}
        hashmapT = {}

        for c in s:
            hashmapS[c] = hashmapS.get(c,0)+1

        for c in t:
            hashmapT[c] = hashmapT.get(c,0)+1

        return hashmapS == hashmapT