class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float('-inf')

        sumx = 0
        for n in nums:
            sumx += n
            maxi = max(maxi, sumx)
            if sumx <0:
                sumx = 0

        return maxi
        


            