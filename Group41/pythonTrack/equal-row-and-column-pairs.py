class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        original_grid=[rows[:] for rows in grid]
        def transpose(grid):
            for i in range(len(grid)):
                for j in range(i+1,len(grid)):
                    grid[i][j],grid[j][i]=grid[j][i],grid[i][j]
            
            return grid

        transposed_grid=transpose(grid)
        res=0

        for row1 in original_grid:
            for row2 in transposed_grid:
                if row1==row2:
                    res+=1
        return res