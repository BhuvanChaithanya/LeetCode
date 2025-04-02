from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)

        for i,v in count.items():
            if v != 1:
                continue
            else:
                k -=1
                if k == 0:
                    return i

        return ""
            


        