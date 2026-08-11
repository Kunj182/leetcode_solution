class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        expected = n * (n + 1) // 2
        actual = sum(nums)
        missing = expected - actual

        return missing

    """
    second-Approach 2

	nums = sorted(nums)
	for i in range (0,len(nums)):
	    if i == nums[i]:
	        i += 1
	        if i == len(nums):
	            print(i)
	    else:
	        print(i)
    """
