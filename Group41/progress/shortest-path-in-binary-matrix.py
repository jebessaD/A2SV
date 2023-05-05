class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        queue = deque()
        queue.append((0,0,1))
        directions = [(0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
        visited = set()

        def inbound(i,j):
            return 0 <= i < len(grid) and 0 <= j < len(grid)
        
        if grid[0][0]:
            return -1

        n = len(grid)
        while queue:
            i , j , path_len = queue.popleft()
            if (i,j) == (n-1,n-1):
                return path_len
   
            for row, col in directions:
                r = row + i
                c = col + j

                if (r,c) not in visited and inbound(r,c) and not grid[r][c]:
                    visited.add((r,c))
                    queue.append((r,c,path_len + 1))

        return -1