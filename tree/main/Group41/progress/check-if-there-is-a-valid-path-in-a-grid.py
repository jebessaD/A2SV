class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        horizontal = {(1,1),(1,3),(1,5),(4,1),(6,1),(4,3),(6,3),(4,5),(6,5)}
        vertical = {(2,2),(2,5),(2,6),(3,2),(4,2),(3,5),(3,6),(4,5),(4,6)}

        parent = {}
        rank = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                parent[(i,j)]=(i,j)
                rank[(i,j)] = 1

        def find(node):
            p = parent[node]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union(n1,n2):
            p1,p2 = find(n1),find(n2)

            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]

        for i in range(len(grid)):
            for j in range(len(grid[0])-1):
                if (grid[i][j],grid[i][j+1]) in horizontal:
                    union((i,j),(i,j+1))
        for i in range(len(grid)-1):
            for j in range(len(grid[0])):
                if (grid[i][j],grid[i+1][j]) in vertical:
                    union((i,j),(i+1,j))

        return find((0,0)) == find((len(grid)-1,len(grid[0])-1))
