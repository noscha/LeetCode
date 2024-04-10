class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        ''' Simulate process '''
        deck.sort()
        res = [-1] * len(deck)
        queue = [i for i in range(len(deck))]

        while queue:
            res[queue.pop(0)] = deck.pop(0)
            if queue: queue.append(queue.pop(0))
        return res
