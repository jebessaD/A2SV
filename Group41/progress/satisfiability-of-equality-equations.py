class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {char:char for char in map(chr, range(97, 123))}
        rank = {char:1 for char in map(chr, range(97, 123))}

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
                

        for n1,sign,_,n2 in equations:
            if sign == "=":
                union(n1,n2)

        for n1,sign,_,n2 in equations:
            if sign == "!" and find(n1) == find(n2):
                return False

        return True
            