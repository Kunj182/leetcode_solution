class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        for i in range (0,len(nums)):
            if i == nums[i]:
                i += 1
                if len(nums) == i:
                    return i
            else:
                return i
                
    """
    second-Approach 2

    n = len(nums)
    expected = n * (n + 1) // 2
    actual = sum(nums)
    missing = expected - actual
    """
