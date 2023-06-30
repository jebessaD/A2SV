class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        parent = [ i for i in range(n+1)]
        rank = [1] * (n + 1)

        def find(node):
            p = parent[node]

            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]

            return p


        def union(i,j):
            p1 = find(i)
            p2 = find(j)
            
            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                parent[p2] = p1
            else:
                rank[p2] += rank[p1]
                parent[p1] = p2
        
        for i in range(n):
            for j in range(n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    union(i,j)

        ans = defaultdict(int)
        for i in range(n):
            ans[find(i)] += 1

        return sum(Counter(ans).values()) - len(ans)