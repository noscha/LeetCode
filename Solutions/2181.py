# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ Iterate over list and sum up """
        dummy = ListNode()
        runner = dummy
        s = 0
        while head:
            s += head.val
            if not head.val and s > 0:
                runner.next = ListNode(val=s)
                runner = runner.next
                s = 0
            head = head.next
        return dummy.next
