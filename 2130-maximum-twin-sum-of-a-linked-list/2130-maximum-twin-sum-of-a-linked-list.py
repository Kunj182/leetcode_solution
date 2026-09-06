# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        values = []
        while head != None:
            values.append(head.val)
            head = head.next
        i = 0
        j = len(values)-1
        max_val = float('-inf')
        while i < j :
            candidate = values[i] + values[j]
            max_val = max(max_val, candidate)
            i += 1
            j -= 1
        return max_val
