import math
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        current_sum = 0
        size = math.inf
        i = 0
        j = 0
        while j < len(nums):
            current_sum = current_sum + nums[j]
            while current_sum >= target:
                size = min(size, j - i + 1)
                current_sum = current_sum - nums[i]
                i += 1
            j += 1
        return 0 if size == math.inf else size

        # for i in range(len(nums)):
        #     sum = 0
        #     for j in range(i,len(nums)):

        #         sum = sum + nums[j]

        #         if sum >= target:
        #             size = min(size, j - i + 1)
        #             break
        


