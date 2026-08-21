# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr1 = l1
        curr2 = l2
        carry = 0
        head = None
        tail = None
        
        while curr1 or curr2 or carry:
            if curr1:
                value1 = curr1.val
            else:
                value1 = 0
            if curr2:
                value2 = curr2.val
            else:
                value2 = 0

            total = value1 + value2 + carry
            digit = total % 10
            carry = total // 10

            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next   

            newNode = ListNode(digit)
            if head == None:
                head = newNode
                tail = newNode
            else:
                tail.next = newNode
                tail = newNode

        return head

    



       