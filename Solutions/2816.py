# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ Run over list from back and double each entry """
        queue = []
        while head:
            queue.append(head.val)
            head = head.next

        queue.reverse()
        overhead = 0
        for i in range(len(queue)):
            temp = queue[i] * 2 + overhead
            queue[i] = temp % 10
            overhead = int(temp >= 10)
        if overhead:
            queue.append(1)

        # Reconstruct List
        dummy = ListNode()
        res = dummy
        for i in queue[::-1]:
            dummy.next = ListNode(i)
            dummy = dummy.next
        return res.next
