class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i,subcur,total):
            if total == target:
                res.append(subcur.copy())
                return
            if total>target or i>= len(candidates):
                return
            subcur.append(candidates[i])

            dfs(i,subcur,total+candidates[i])
            subcur.pop()
            dfs(i+1, subcur, total)

        dfs(0,[],0)
        return res
