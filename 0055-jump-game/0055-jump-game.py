class Solution:
    def canJump(self, nums: List[int]) -> bool:
        final = len(nums)-1

        for i in range(len(nums)-2,-1,-1):
            if nums[i]+i >= final:
                final = i

        return final==0

