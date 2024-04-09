class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ''' If an entry larger or equal than tickets[k] it will appear tickets[k] times,
            if an entry is smaller, it will appear according to its amount '''
        res = 0
        for i in range(len(tickets)):
            if tickets[i] >= tickets[k]:
                res += tickets[k] - int(i > k)
            else:
                res+= tickets[i]
        return res
