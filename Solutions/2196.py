# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        """
        Iterate over descriptions and create nodes or access through hash map.
        Root is the only node which is never on children position.
        """
        hm, hs = {}, set()

        for p, c, l in descriptions:
            if p not in hm:
                hm[p] = TreeNode(val=p)

            hs.add(c)
            if c not in hm:
                hm[c] = TreeNode(val=c)
                
            if l:
                hm[p].left = hm[c]
            else:
                hm[p].right = hm[c]

        for p, _, _ in descriptions:
            if p not in hs:
                return hm[p]
