class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        counts1 ={}
        counts2 = {}

        for i in range(len(s1)):
            counts1[s1[i]] = counts1.get(s1[i], 0) +1
            counts2[s2[i]] = counts2.get(s2[i], 0) + 1
        
        for j in range(len(s1), len(s2)):
            if counts1 == counts2:
                return True

            else:
                counts2[s2[j-len(s1)]] -= 1
                if counts2[s2[j-len(s1)]] == 0:
                    del counts2[s2[j - len(s1)]]

                counts2[s2[j]] = counts2.get(s2[j],0)+1

        return counts1 == counts2


            
