class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        ans=0
        for i in range(1,len(grid)-1):
            for j in range(1,len(grid[0])-1):
                res=max(ans,sum(grid[i-1][j-1:j+2] ) + grid[i][j] + sum(grid[i+1][j-1:j+2])) 
                ans=res
        return res
                
                