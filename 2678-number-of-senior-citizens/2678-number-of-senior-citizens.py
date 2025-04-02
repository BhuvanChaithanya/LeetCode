class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0

        for c in details:
            if int(c[11:13])>60:
                count += 1

        return count