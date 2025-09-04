class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashs = {}

        for i in range(len(nums)):
            if (target - nums[i]) in hashs:
                return [i,hashs[(target - nums[i])]]

            else:
                hashs[nums[i]] = i

        