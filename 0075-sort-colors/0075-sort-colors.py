class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = [0]*3
        for num in nums:
            freq[num] += 1
        k = 0
        nums.clear()
        while k <=2:
            f = freq[k]
            while f:
                nums.append(k)
                f -=1
            k +=1
            
        