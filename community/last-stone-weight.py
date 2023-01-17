class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=list(map(lambda x:-x ,stones))
        heapq.heapify(stones)
        l=len(stones)
        x=0
        for i in range(l):
            if len(stones)<=1:break
            x=heapq.heappop(stones)
            y=heapq.heappop(stones)
            if x-y:heapq.heappush(stones,x-y)
            
        if stones:return -heapq.heappop(stones)
        return 0
            