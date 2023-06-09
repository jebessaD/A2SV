class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        queue = deque()
        queue2 = deque()
        visited = set()
        visited2 = set()
        def inbound(i,j):
            return 0 <= i < len(grid) and 0<= j < len(grid[0])
        
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        first_island_i, first_island_j = -1,-1
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 1:
                    first_island_i,first_island_j = i,j
                    break

        queue.append((first_island_i,first_island_j))
        visited.add((first_island_i,first_island_j))
        while queue:
            m,n = queue.popleft()
            queue2.append((m,n,0))
            for x,y in directions:
                if inbound(x+m,y+n) and grid[x+m][y+n] == 1 and (x+m,y+n) not in visited:
                    queue.append((x+m,y+n))
                    visited.add((x+m,y+n))

        min_level = len(grid)
        while queue2:
            m,n,level = queue2.popleft()
            for x,y in directions:
                if inbound(x+m,y+n) and (x+m,y+n) not in visited2:
                    queue2.append((x+m,y+n,level + 1))
                    visited2.add((x+m,y+n))
                    if grid[x+m][n+y] == 1 and (x+m,y+n) not in visited :
                        
                        min_level = min(min_level, level)

        return min_level
