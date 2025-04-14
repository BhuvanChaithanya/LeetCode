class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        left_cnt = defaultdict(int)
        right_cnt = Counter(nums)

        for i in range(len(nums)):
            left_cnt[nums[i]] += 1
            right_cnt[nums[i]] -= 1

            left_len = i+1
            right_len = len(nums)-i-1

            if (2*left_cnt[nums[i]] > left_len) and (2*right_cnt[nums[i]] > right_len):
                return i

        return -1

