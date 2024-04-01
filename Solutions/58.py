class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ''' Look for last word from the end '''
        count, flag = 0, 0
        for i in range(len(s)):
            if s[- (i + 1)] != ' ':
                count += 1
                flag = 1
            if s[- (i + 1)] == ' ' and flag:
                return count
        return count
