class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        c_sum = 0
        for i in range(k):
            c_sum = c_sum + nums[i]
        max_num = c_sum
        for i in range(k, len(nums)):
            c_sum = c_sum + nums[i]
            c_sum = c_sum - nums[i - k]
            max_num = max(max_num, c_sum)
        return max_num / k