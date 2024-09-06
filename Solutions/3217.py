# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        """ Traverse over list and check if node in nums """

        res = ListNode()
        new_head = res
        nums = set(nums)

        while head:

            if head.val in nums:
                head = head.next
                continue

            new_node = ListNode(val=head.val)
            new_head.next = new_node
            new_head = new_node
            head = head.next

        return res.next
            
