class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ''' Iterate over string two times(back and forward), to remove invalid closing brackets '''
        res, temp = [], []
        count = 0
        for i in s:
            if i == '(':
                count += 1
                temp.append(i)
            elif i == ')' and count > 0:
                count -= 1
                temp.append(i)
            elif i not in ('(', ')'):
                temp.append(i)

        count = 0
        for i in temp[::-1]:
            if i == ')':
                count += 1
                res.append(i)
            elif i == '(' and count > 0:
                count -= 1
                res.append(i)
            elif i not in ('(', ')'):
                res.append(i)
        
        return "".join(res[::-1])
