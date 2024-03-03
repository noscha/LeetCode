# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ''' First pointe at beginning, second at beginning + n. Iterate until second
            pointer is at the end. Then remove elemnt next to first pointer '''
        
        res = ListNode(0, head)
        nNode = head
        head = res

        for i in range(n):
            nNode = nNode.next

        while nNode:
            head = head.next
            nNode = nNode.next

        head.next = head.next.next
        return res.next
