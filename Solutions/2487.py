# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ Put list into monotonic stack """
        monotonic_stack = []

        while head:
            while monotonic_stack and monotonic_stack[-1] < head.val:
                monotonic_stack.pop()
            monotonic_stack.append(head.val)
            head = head.next
        
        # Reconstruct List
        temp = ListNode()
        res = temp
        for i in monotonic_stack:
            temp.next = ListNode(i)
            temp = temp.next
        return res.next
      
