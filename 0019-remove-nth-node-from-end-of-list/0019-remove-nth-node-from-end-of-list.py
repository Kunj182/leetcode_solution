# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        length = 0 
        l = head
        while l != None:
            length = length + 1
            l = l.next
        d = length - n + 1
        prev = dummy
        i = 0
        while i < (d - 1):
            prev = prev.next
            i = i + 1
        prev.next = prev.next.next
        return dummy.next