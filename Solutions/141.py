# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ''' Iterate over list and store which nodes were visited  '''
        visited = set()
        while head != None:
            if head not in visited:
                visited.add(head)
            else:
                return True
            head = head.next
        return False
