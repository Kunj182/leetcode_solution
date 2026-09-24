import math
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        sum = 0
        size = math.inf
        i = 0
        j = 0
        while j < len(nums):
            sum = sum + nums[j]
            while sum >= target:
                size = min(size, j - i + 1)
                sum = sum - nums[i]
                i += 1
            j += 1

        # for i in range(len(nums)):
        #     sum = 0
        #     for j in range(i,len(nums)):

        #         sum = sum + nums[j]

        #         if sum >= target:
        #             size = min(size, j - i + 1)
        #             break
        return 0 if size == math.inf else size


