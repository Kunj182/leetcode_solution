class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        stack = []
        for i in range(2 * n):
            curr_num = nums[i % n]
            while stack and nums[stack[-1]] < curr_num:
                 ans[stack.pop()]=curr_num
            if i < n:
                stack.append(i)
        return ans