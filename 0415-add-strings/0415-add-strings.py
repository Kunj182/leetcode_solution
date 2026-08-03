class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i = len(num1) -1
        j = len(num2) -1
        carry = 0
        result = []

        while i >=0 or j>=0 or carry:

            if i>=0:
                value1 = int(num1[i])
            else:
                value1 = 0
            
            if j>=0:
                value2 = int(num2[j])
            else:
                value2 = 0
            
            total = value1 + value2 + carry
            digit = total % 10
            carry = total // 10

            result.append(str(digit))
            i -= 1
            j -= 1

        result = result[::-1]
        answer = "".join(result)

        return answer
