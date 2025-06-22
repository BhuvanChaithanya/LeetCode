class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = set()
        subset = []
        def dfs(i,subcur,total):
            if total == target:
                res.add(tuple(subcur))
                return
            if total>target or i>= len(candidates):
                return
            subcur.append(candidates[i])
            dfs(i+1,subcur,total+candidates[i])
            subcur.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, subcur, total)
        dfs(0,[],0)
        return list(res)