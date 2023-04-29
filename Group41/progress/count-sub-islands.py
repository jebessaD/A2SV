class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def inbound(i,j):
            return 0 <= i < len(grid1) and 0 <= j < len(grid1[0])
            
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        visited = set()
        self.flag = True
        def dfs(i,j):
            visited.add((i,j))
            if not grid1[i][j]:
                self.flag = False
                    
            for row, col in directions:
                new_row = i + row
                new_col = j + col
                if (new_row,new_col) not in visited and inbound(new_row,new_col) and grid2[new_row][new_col]:
                    dfs(new_row,new_col)
        ans = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                self.flag = True
                if (i,j) not in visited and grid2[i][j]:
                    dfs(i,j)
                    if self.flag:
                        ans += 1              

        return ans
        