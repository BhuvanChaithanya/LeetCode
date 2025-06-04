class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float('-inf')

        res = 0 

        for i in range(len(nums)):
            res += nums[i]

            maxi = max(res, maxi)
            
            if res <0:
                res = 0


        return maxi

            