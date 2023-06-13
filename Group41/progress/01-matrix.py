class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        def inBound(i,j):
            return 0 <= i < len(mat) and 0<= j < len(mat[0])

        queue = deque()
        visited = set()

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i,j))
                    visited.add((i,j))

        while queue:
            parent_i, parent_j = queue.popleft()

            for r,c in directions:
                child_i,child_j = parent_i + r, parent_j + c

                if inBound(child_i,child_j) and (child_i,child_j) not in visited:
                    queue.append((child_i,child_j))
                    visited.add((child_i,child_j))
                    mat[child_i][child_j] += mat[parent_i][parent_j]

        return mat

        