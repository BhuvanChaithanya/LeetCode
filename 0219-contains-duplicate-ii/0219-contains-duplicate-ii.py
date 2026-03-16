class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}#num -> ind

        for i,val in enumerate(nums):
            if val in hashmap:
                if i - hashmap[val] <= k:
                    return True

            
            hashmap[val] = i

        return False
