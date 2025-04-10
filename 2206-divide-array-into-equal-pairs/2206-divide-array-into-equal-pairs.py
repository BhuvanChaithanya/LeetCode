class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = Counter(nums)

        for v, c in count.items():
            if c%2 != 0:
                return False

        return True