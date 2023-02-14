class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        ans = 0
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0

        for i in range(1,len(grid)-1):
            for j in range(1,len(grid[0])-1):
                summation = set()
                elements = []
                diagonal1 = grid[i+1][j+1] + grid[i-1][j-1]  + grid[i][j]
                diagonal2 = grid[i-1][j+1] + grid[i+1][j-1] + grid[i][j]
                summation.add(diagonal1)
                summation.add(diagonal2)
                for k in range(3):
                    summation.add(sum(grid[i-1+k][j-1:j+2]))
                    elements.extend(grid[i-1+k][j-1:j+2])

                for z in range(3):
                    col_sum =  grid[i-1][j-1+z] + grid[i][j-1+z] + grid[i + 1][j - 1 + z] 
                    summation.add(col_sum)

                ele_size = len(set(elements)) == 9
                sum_equality = len(summation) == 1
                min_element = min(elements) == 1
                max_element = max(elements) == 9

                if ele_size and sum_equality and min_element and max_element :
                    ans += 1

        return ans
        