class Solution:
    def minOperations(self, logs: List[str]) -> int:
        """ Manage folders through stack """
        stack = []
        for i in logs:
            if i == './':
                pass
            elif i == "../":
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        return len(stack)
