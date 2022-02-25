class Solution:
    def reversePairs(self, nums) -> int:
        start = 0
        end = len(nums) - 1
        return self._reversePairs(nums, start, end)

    def _reversePairs(self, nums, start, end):
        if start >= end:
            return 0
        count = 0
        mid = (start + end) // 2
        count += self._reversePairs(nums, start, mid)
        count += self._reversePairs(nums, mid + 1, start)
        count += self.count_reverse_pairs(nums, start, mid, mid + 1, end)

        self.merge(nums, start, mid, mid + 1, end)
        return count

    def merge(self, nums, left_s, left_e, right_s, right_e):
        while left_s <= left_e:
            if nums[left_s] > nums[right_s]:
                nums[left_s], nums[right_s] = nums[right_s], nums[left_s]
                temp = right_s + 1
                while temp < right_e and nums[temp] < nums[temp - 1]:
                    nums[temp], nums[temp - 1] = nums[temp - 1], nums[temp]
                    temp += 1
            left_s += 1

    def count_reverse_pairs(self, nums, s_l, s_r, e_l, e_r):
        c = 0
        while s_l <= s_r and e_l <= e_r:
            while s_l <= s_r and nums[s_l] <= 2 * nums[e_l]:
                s_l += 1
            if s_l <= s_r:
                c += s_r - s_l + 1
            e_l += 1
        return c


s = Solution()
nums = [233, 2000000001, 234, 2000000006, 235, 2000000003, 236, 2000000007, 237, 2000000002, 2000000005, 233, 233, 233,
        233, 233, 2000000004]
print(s.reversePairs(nums))
