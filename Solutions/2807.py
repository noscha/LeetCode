# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ Add gcd in between nodes """

        def euclidean(a, b):
            while b:
                a, b = b, a % b
            return a

        res = head
        while head.next:

            new_node = ListNode(val=euclidean(head.val, head.next.val), next=head.next)
            head.next = new_node
            head = head.next.next

        return res
