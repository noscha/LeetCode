class Solution:
    def clearDigits(self, s: str) -> str:
        """
        Use stack, if element is number pop it and previous entry
        """

        stack = []

        for i in s:
            stack.append(i)

            if 48 <= ord(i) <= 57:
                stack.pop()
                stack.pop()

        return "".join(stack)
