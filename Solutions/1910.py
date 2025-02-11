class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        """
        Put chars into stack and check if last three elements form "part"
        """

        stack = []
        part = list(part)
        for i in s:
            stack.append(i)
            
            while len(stack) >= len(part) and stack[-len(part):] == part:
                stack = stack[:-len(part)]

        return "".join(stack)
