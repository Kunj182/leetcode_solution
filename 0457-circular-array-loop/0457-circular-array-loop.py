class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:

        
        def next_index(current,direction):
            
                next_index = (current + nums[current])%n
                if next_index == current:
                    return -1
                if (nums[current]>0)!= direction:
                    return -1
                return next_index
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                continue
            direction = nums[i] > 0
            slow = i
            fast = i
            while True:
                slow = next_index(slow,direction)
                if slow == -1:
                    break
                fast = next_index(fast,direction)
                if fast == -1:
                    break
                fast = next_index(fast,direction)
                if fast == -1:
                    break
                if slow == fast:
                    return True
            current = i
            while nums[current] != 0 and (nums[current] > 0) == direction:
                next_idx = (current + nums[current]) % n
                nums[current] = 0
                current = next_idx
        return False