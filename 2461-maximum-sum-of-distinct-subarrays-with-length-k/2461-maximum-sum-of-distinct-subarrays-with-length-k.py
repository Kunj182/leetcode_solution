from collections import defaultdict


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_num = 0
        curr_sum = 0
        dups = 0

        my_map = defaultdict(int)
        for i in range(k):
            my_map[nums[i]] += 1
            curr_sum = curr_sum + nums[i]

            if my_map.get(nums[i], 0) > 1:
                dups = dups + 1

        if dups == 0:
            max_num = max(max_num, curr_sum)
        for i in range(k, len(nums)):
            num_to_add = nums[i]
            num_to_remove = nums[i - k]
            if num_to_add not in my_map:
                my_map[num_to_add] = 0
            my_map[num_to_add] = my_map.get(num_to_add, 0) + 1
            if my_map[num_to_add] > 1:
                dups = dups + 1
            curr_sum = curr_sum + num_to_add
            if my_map.get(num_to_remove, 0) > 1:
                dups = dups - 1
            my_map[num_to_remove] = my_map.get(num_to_remove, 0) - 1
            curr_sum = curr_sum - num_to_remove
            if dups == 0:
                max_num = max(max_num, curr_sum)
        return max_num