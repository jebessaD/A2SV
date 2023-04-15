class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        directions = [(0,1),(0,-1),(-1,0),(1,0)]
        def inbound(row, col):
            return 0 <= row < len(image) and 0 <= col < len(image[0])

        visited = set()
        start_val = image[sr][sc]
        def dfs(sr, sc):
            if image[sr][sc] == start_val:
                image[sr][sc] = color

            for i,j in directions:
                row, col = sr + i , sc + j
                if (row,col) not in visited and inbound(row,col) and image[row][col] == start_val :
                    visited.add((row,col))
                    dfs(row,col)

        dfs(sr,sc)
        return image