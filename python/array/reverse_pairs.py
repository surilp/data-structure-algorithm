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
        count += self._reversePairs(nums, mid + 1, end)
        count += self.count_reverse_pairs(nums, start, mid, mid + 1, end)

        self.merge_with_new_array(nums, start, mid, mid + 1, end)
        return count

    def merge(self, nums, left_s, left_e, right_s, right_e):
        while left_s <= left_e:
            if nums[left_s] > nums[right_s]:
                nums[left_s], nums[right_s] = nums[right_s], nums[left_s]
                temp = right_s + 1
                while temp <= right_e and nums[temp] < nums[temp - 1]:
                    nums[temp], nums[temp - 1] = nums[temp - 1], nums[temp]
                    temp += 1
            left_s += 1

    def merge_with_new_array(self, nums, left_s, left_e, right_s, right_e):
        l_s = left_s
        l_e = left_e
        r_s = right_s
        r_e = right_e

        temp = [None] * ((left_e - left_s + 1) + (right_e - right_s + 1))
        temp_i = 0
        while left_s <= left_e and right_s <= right_e:
            if nums[left_s] <= nums[right_s]:
                temp[temp_i] = nums[left_s]
                left_s += 1
            else:
                temp[temp_i] = nums[right_s]
                right_s += 1
            temp_i += 1
        while left_s <= left_e:
            temp[temp_i] = nums[left_s]
            temp_i += 1
            left_s += 1
        while right_s <= right_e:
            temp[temp_i] = nums[right_s]
            temp_i += 1
            right_s += 1

        left_s = l_s
        left_e = l_e
        right_s = r_s
        right_e = r_e

        temp_i = 0
        while left_s <= left_e:
            nums[left_s] = temp[temp_i]
            temp_i += 1
            left_s += 1
        while right_s <= right_e:
            nums[right_s] = temp[temp_i]
            temp_i += 1
            right_s += 1

        while left_s <= left_e:
            if nums[left_s] > nums[right_s]:
                nums[left_s], nums[right_s] = nums[right_s], nums[left_s]
                temp = right_s + 1
                while temp <= right_e and nums[temp] < nums[temp - 1]:
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
nums = [233, 501, 234, 506, 235, 503, 236, 507, 237, 502, 505, 233, 233, 233,
        233, 233, 504]
print(s.reversePairs(nums))

s = Solution()
nums = [40, 25, 19, 12, 9, 6, 2]
print(s.reversePairs(nums))
