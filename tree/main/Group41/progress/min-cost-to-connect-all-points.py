class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        parent = [ i for i in range(len(points)+1)]
        rank = [1] * (len(points) + 1)

        def find(node):
            p = parent[node]
            while p != parent[p]:
                parent[p]= parent[parent[p]]
                p = parent[p]

            return p

        def union(n1,n2):
            p1,p2 = find(n1),find(n2)

            if rank[p1] > rank[p2]:
                parent[p2] =  p1
                rank[p1] += rank[p2]
            else:
                parent[p1] =  p2
                rank[p2] += rank[p1]

        def manhattanDistance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        connections = []
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                dist = manhattanDistance(points[i],points[j])
                connections.append((dist,i,j))


        connections.sort()
        ans = 0
        for con in connections:
            dist,i,j = con
            if find(i) != find(j):
                union(i,j)
                ans += dist

        return ans 
        