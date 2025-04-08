class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        cnt = [0]*101

        for i in range(len(heights)):
            cnt[heights[i]] += 1
        exp = []

        for i in range(1,101):
            c = cnt[i]
            for _ in range(c):
                exp.append(i)

        res = 0

        for i in range(len(exp)):
            if exp[i] != heights[i]:
                res += 1

        return res