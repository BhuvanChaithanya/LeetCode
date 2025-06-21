class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            while l<r:
                total = nums[i]+nums[l]+nums[r]
                
                
                if total == 0 and l<r:
                    res.append([nums[i], nums[l], nums[r]])
                    l +=1

                elif total >0 and l<r:
                    r -=1
                elif total <0 and l<r:
                    l +=1

        return res