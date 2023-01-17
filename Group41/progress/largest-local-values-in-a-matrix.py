class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        matrix=[]
        for i in range(1,len(grid)-1):
            row=[]
            for j in range(1,len(grid[0])-1):
                maximum=0
                for index in range(i-1,i+2):    
                    temp=max(grid[index][j-1:j+2])
                    maximum=max(maximum,temp)
                row.append(maximum)

            matrix.append(row)

        return matrix
