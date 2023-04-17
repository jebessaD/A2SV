class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
                

        visited = set()
        self.max_area = 0
        self.area = 0
        directions  = [(0,1),(0,-1),(1,0),(-1,0)]

        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def dfs(i,j):
            visited.add((i, j))
            for row , col in directions:
                
                new_row = i + row 
                new_col = j + col
                
                if not (new_row, new_col) in visited and inbound(new_row,new_col) and grid[new_row][new_col] == 1:
                    self.area += 1
                    
                    dfs(new_row,new_col)
                    

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if (i,j) not in visited and grid[i][j] == 1:
                    dfs(i,j)
                    
                    self.max_area = max(self.max_area,self.area + 1)
                    self.area = 0
                    
        return self.max_area
