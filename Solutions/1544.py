class Solution:
    def makeGood(self, s: str) -> str:
        ''' Keep track of letter pairs with a stack '''
        stack = []
        for i in range(len(s)):
            stack.append(s[i])
            while len(stack) >= 2 and abs(ord(stack[-1]) - ord(stack[-2])) == 32:
                stack.pop()
                stack.pop()

        return "".join(stack)
