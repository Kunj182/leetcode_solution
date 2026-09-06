# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        def reverselist(head_node): 
            prev = None
            curr = head_node
            while curr is not None:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        p1 = head
        p2 = reverselist(slow)
        max_val = float('-inf')
        while p1 != None and p2 != None:
            candidate = p1.val + p2.val
            max_val = max(max_val, candidate)
            p1 = p1.next
            p2 = p2.next
        return max_val