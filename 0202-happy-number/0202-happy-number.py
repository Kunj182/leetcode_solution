class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n
        def sumofsquere(n):
            sum = 0
            while n > 0:
                dig = n % 10
                sum = sum + (dig * dig)
                n = n // 10
            return sum
        while True:
            slow = sumofsquere(slow)
            fast = sumofsquere(sumofsquere(fast))

            if slow == fast:
                break

        if fast == 1:
            return True
        else:
            return False
