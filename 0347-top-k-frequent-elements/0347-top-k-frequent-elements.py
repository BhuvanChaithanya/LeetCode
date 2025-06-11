class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_freq = {}
        freq_to_num = [[] for i in range(len(nums)+1)]

        for n in nums:
            num_to_freq[n] = num_to_freq.get(n,0)+1

        for key, v in num_to_freq.items():
            freq_to_num[v].append(key)
        res = []
        
        for i in range(len(freq_to_num)-1,0,-1):
            for num in freq_to_num[i]:
                res.append(num)
                if len(res)==k:
                    return res
                

        return res