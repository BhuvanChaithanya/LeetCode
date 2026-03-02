import math
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = defaultdict(int)
        res = []
        for num in nums:
            hashmap[num] += 1

        for num,freq in hashmap.items():
            if freq > math.floor(len(nums)/3):
                res.append(num)

        return res