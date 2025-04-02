class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        maxi = 0
        count_inc = 0
        count_dec = 0
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                count_inc +=1
                count_dec = 0
                maxi = max(maxi, count_inc)

            elif nums[i-1] > nums[i]:
                count_dec += 1
                count_inc = 0
                maxi = max(maxi, count_dec)

            else:
                count_dec = 0
                count_inc = 0

        return maxi+1