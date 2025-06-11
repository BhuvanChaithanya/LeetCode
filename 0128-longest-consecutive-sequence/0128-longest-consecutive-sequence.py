class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        res = 0
        for num in numset:
            curr = 0
            if num-1 not in numset:
                while num+curr in numset:
                    curr += 1

                res = max(res,curr)

        return res
