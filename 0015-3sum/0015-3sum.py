class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            if a>0:
                break
            
            elif i>0 and nums[i] == nums[i-1]:
                continue

            tar = nums[i]

            l,r = i+1, len(nums)-1

            while l<r:
                if nums[l] + nums[r] > (-tar):
                    r -= 1
                elif nums[l] + nums[r] < (-tar):
                    l += 1
                else:
                    res.append([nums[l], tar, nums[r]])
                    l += 1
                    r -= 1

                    while nums[l] == nums[l-1] and l<r:
                        l += 1
        return res
                    