class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ''' If an entry larger or equal than tickets[k] it will appear tickets[k] times,
            if an entry is smaller, it will appear according to its amount '''
        res = 0
        for i in tickets:
            if i >= tickets[k]:
                res += tickets[k]
            else:
                res+= i
        return res
