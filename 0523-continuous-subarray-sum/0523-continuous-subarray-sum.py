class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = {0: -1}
        total = 0

        for i, n in enumerate(nums):
            total += n
            if total %k not in remainder:
                remainder[total%k] = i

            elif total %k in remainder and i - remainder[total%k] >=2:
                return True

        
        return False