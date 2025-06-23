class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxl, maxr = height[l], height[r]
        res = 0
        while l<r:
            if maxl<= maxr:
                res += (maxl - height[l]) if (maxl - height[l]) >0 else 0
                maxl = max(maxl, height[l])
                l += 1
                
            else:
                res += (maxr - height[r]) if (maxr - height[r]) >0 else 0
                maxr = max(maxr, height[r])
                r -= 1
        return res


