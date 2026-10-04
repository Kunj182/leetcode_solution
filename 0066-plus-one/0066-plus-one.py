class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        i = len(digits) - 1
        for i in range(len(digits)-1, -1, -1):  
            if digits[i] == 9:
                digits[i] = 0
                i -= 1
            else:
                digits[i] = digits[i] + 1
                break
        if i < 0:
            digits.insert(0,1)
        return digits

