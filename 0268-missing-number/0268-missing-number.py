class Solution:
    def missingNumber(self, nums: List[int]) -> int:


	    nums = sorted(nums)
	    for i in range (0,len(nums)):
	        if i == nums[i]:
	            i += 1
	            if i == len(nums):
	                return(i)
	        else:
	            return(i)

