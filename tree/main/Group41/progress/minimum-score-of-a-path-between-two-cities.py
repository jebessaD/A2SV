class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parent = [i for i in range(n +1)]
        rank = [1] * (n+1)

        def find(node):
            p = parent[node]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]

            return p

        self.ans = float("inf")
        def union(node1,node2,distance):
            p1,p2= find(node1), find(node2)

            if rank[p1] < rank[p2]:
                rank[p2] += rank[p1]
                parent[p1] = p2
            else:
                rank[p1] += rank[p2]
                parent[p2] = p1

        for n1,n2,d in roads:
            union(n1,n2,d)

        ans=float("inf")
        for start,end,distance in roads:
            if find(start) == find(end) == find(1):
                ans=min(ans,distance)
        return ans
