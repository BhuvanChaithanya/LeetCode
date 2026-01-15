class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq_map = {}
        for n in nums:
            freq_map[n] = freq_map.get(n,0)+1
        rev_freq = {}
        maxi = float('-inf')
        for num,freq in freq_map.items():
            rev_freq[freq] = num
            maxi = max(maxi, freq)

        if maxi >(len(nums)//2):
            return(rev_freq[maxi])
        
