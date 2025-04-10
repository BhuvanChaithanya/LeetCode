class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        extend = nums+ nums

        size = 1

        for i in range(1,len(extend)):
            if size == n:
                    return True
            if extend[i-1] <= extend[i]:
                
                size += 1

                

            else:
                size = 1

        
        return False
