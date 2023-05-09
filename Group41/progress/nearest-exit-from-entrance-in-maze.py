class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        queue = deque()
        queue.append((entrance[0],entrance[1],0))

        def inbound(i,j):
            return 0 <= i < len(maze) and 0 <= j < len(maze[0])
        visited = set()
        while queue:

            row,col,path = queue.popleft()
            for i,j in directions:
                r = row + i
                c = col + j
                if not inbound(r,c) and (row,col) != (entrance[0],entrance[1]):
                    return path

                if (r,c) not in visited and inbound(r,c) and maze[r][c] == ".":
                    queue.append((r,c,path + 1))
                    visited.add((r,c))

        return -1
        