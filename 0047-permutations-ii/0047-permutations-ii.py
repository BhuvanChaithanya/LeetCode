class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        if len(nums) == 0:
            return [[]]
        
        perms = self.permuteUnique(nums[1:])

        for p in perms:
            
            for i in range(len(p)+1):
                p_copy = p.copy()
                p_copy.insert(i,nums[0])
                res.add(tuple(p_copy))
            



        return [list(x) for x in res]