# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        """ Split list into equal segments """

        length = 0
        curr = head
        # get length
        while curr:
            length += 1
            curr = curr.next

        curr = head
        segment_lenght, mod = length // k, length % k
        res = []
        for _ in range(k):
            res.append(curr)

            print(bool(mod), mod)
            for __ in range(segment_lenght - 1 + bool(mod)):
                if curr: curr = curr.next

            mod = max(0, mod - 1)

            if curr:
                curr.next, curr = None, curr.next

        return res
