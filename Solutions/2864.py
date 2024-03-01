class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ''' Count occurrence of ones and build string '''

        count = 0
        for i in s:
            if i == '1':
                count += 1
        
        return ''.join((['1'] * (count - 1)) + (['0'] * (len(s) - count)) + ['1'])
