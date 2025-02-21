# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):

        """
        Traverse tree with bfs to recover nodes
        """

        self.nodes = set([0])

        root.val = 0
        queue = [root]
        while queue:
            cur = queue.pop(0)

            if cur.left:
                queue.append(cur.left)
                val = 2 * cur.val + 1
                cur.left.val = val
                self.nodes.add(val)

            if cur.right:
                queue.append(cur.right)
                val = 2 * cur.val + 2
                cur.right.val = val
                self.nodes.add(val)

    def find(self, target: int) -> bool:
        return target in self.nodes


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
