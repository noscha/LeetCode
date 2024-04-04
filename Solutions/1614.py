class Solution:
    def maxDepth(self, s: str) -> int:
        ''' Keep track of bracket pairs with a stack '''
        res, temp = 0, 0
        stack = []
        for i in s:
            if i == ')':
                stack.pop()
                temp -= 1
            if i == '(':
                stack.append(i)
                temp += 1
                res = max(temp, res)
        return res
