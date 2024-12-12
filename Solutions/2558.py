class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        """
        Use min heap with negatives; remove the largest elements with its square root
        """
        heap = [-i for i in gifts]
        heapify(heap)
        
        for _ in range(k):
            element = -(heappop(heap))
            heappush(heap, -(int(sqrt(element))))

        return int(-(sum(heap)))
