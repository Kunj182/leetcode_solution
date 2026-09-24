import math
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        current_sum = 0
        size = math.inf
        left = 0
        
       
        for right, val in enumerate(nums):
            current_sum += val
            
            while current_sum >= target:
                current_size = right - left + 1
                if current_size < size:
                    size = current_size
                
                current_sum -= nums[left]
                left += 1
                
        return 0 if size == math.inf else size
        # for i in range(len(nums)):
        #     sum = 0
        #     for j in range(i,len(nums)):

        #         sum = sum + nums[j]

        #         if sum >= target:
        #             size = min(size, j - i + 1)
        #             break
        


