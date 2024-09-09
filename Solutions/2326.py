# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        """ Simulate """

        res = [[-1] * n for _ in range(m)]

        x, y = 0, 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        d = 0
        d_x, d_y = 1, 0
        while head:
            res[y][x] = head.val
            head = head.next
            
            # check if borders consistent and field occupied
            if not 0 <= x + d_x < n or not 0 <= y + d_y < m or res[y + d_y][x + d_x] != -1:
                d = (d + 1) % 4
            
            d_x, d_y = directions[d][0], directions[d][1]
            x, y = x + d_x, y + d_y

        return res
