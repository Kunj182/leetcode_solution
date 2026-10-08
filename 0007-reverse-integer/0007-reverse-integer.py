class Solution:
    def reverse(self, x: int) -> int:
        reverse = 0   
        nagative = x < 0 
        x = abs(x)
        while x != 0:
            digit = x % 10
            reverse = reverse * 10 + digit
            x = x // 10
        if nagative:
            reverse = reverse * -1
        if reverse < -2147483648 or reverse > 2147483647:
            return 0
        return reverse
