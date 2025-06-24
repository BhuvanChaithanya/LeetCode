class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        l = 0
        count  =0
        for r in range(len(nums)):
            count += nums[r]
            while count >= target:
                res = min(res, r-l+1)
                count -= nums[l]
                l +=1

        if res == float('inf'):
            return 0
        else:
            return res
            