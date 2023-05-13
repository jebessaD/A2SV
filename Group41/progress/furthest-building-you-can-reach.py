class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        difference = [] 
        for i in range(1,len(heights)):
            diff = heights[i] - heights[i-1]
            if diff > 0:
                difference.append(diff)
            else:
                difference.append(0)
        
        heap = []
        for index,num in enumerate(difference):
            if not ladders and num > bricks:
                return index
            
            if bricks >= num:
                heappush(heap,-num)
                bricks -= num
            elif ladders:
                heappush(heap,-num)
                max_ = -heappop(heap)
                bricks += (max_ - num)

                ladders -= 1
            

        return len(heights) - 1