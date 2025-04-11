class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic = {}

        for h,n in zip(heights, names):
            dic[h] = n

        res = []

        for h in reversed(sorted(heights)):
            res.append(dic[h])

        return res