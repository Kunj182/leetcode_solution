class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)

        i = 0
        j = len(nums)-1
        count = 0
        while i < j:
            if nums[i] + nums[j] < target:
                count = count + (j - i)
                i += 1
            else:
                j -= 1

        return count



