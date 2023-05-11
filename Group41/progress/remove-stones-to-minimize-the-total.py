class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap=list(map(lambda x:-x,piles))
        heapify(heap)
        for i in range(k):
            heappush(heap,heappop(heap)//2)
        return -sum(heap)
