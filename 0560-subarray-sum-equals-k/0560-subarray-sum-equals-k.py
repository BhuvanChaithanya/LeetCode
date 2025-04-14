class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum1 = 0
        res = 0
        prefix_freq = {0:1}
        for i in range(len(nums)):
            sum1 += nums[i]
            if (sum1-k) in prefix_freq:
                res += prefix_freq[(sum1-k)]

            prefix_freq[sum1] = prefix_freq.get(sum1,0)+1

        return res





