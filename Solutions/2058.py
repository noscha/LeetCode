# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        """ Iterate over list to get all cp-indexes and remember the smallest one """
        i = 0
        prev = head.val
        fcp, lcp = -1, -1
        md = float("inf")

        while head.next:
            if prev < head.val and head.val > head.next.val or prev > head.val and head.val < head.next.val:
                if fcp == -1:
                    fcp = i
                    lcp = i
                md = i - lcp if i - lcp < md and i - lcp > 0 else md
                lcp = i
            i += 1
            prev = head.val
            head = head.next

        if md == float("inf"):
            return [-1, -1]
        return [md, lcp -fcp]
