class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                left, right = j+1,n-1

                while left < right:
                    if nums[i]+nums[j]+nums[left]+nums[right] > target:
                        right -= 1
                    elif nums[i]+nums[j]+nums[left]+nums[right] < target:
                        left +=1

                    else:
                        res.append([nums[i],nums[j], nums[left], nums[right]])

                        left += 1
                        right -=1
                        while left <right and nums[left] == nums[left-1]:
                            left +=1

        return res
