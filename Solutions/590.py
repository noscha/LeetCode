"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        """ First check all children than root """
        res = []
        
        def dfs(node):
            if not node:
                return

            for i in node.children:
                dfs(i)
            res.append(node.val)

        dfs(root)
        return res
