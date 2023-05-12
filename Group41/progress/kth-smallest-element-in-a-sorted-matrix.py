class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        heap = []
        kth = len(matrix)**2 - k + 1
        for row in matrix:
            for num in row:
                heappush(heap,num)
                if len(heap) > kth:
                    heappop(heap)
                
        return heappop(heap)


