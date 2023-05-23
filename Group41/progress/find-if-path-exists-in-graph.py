class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parents = [i for i in range(n)]
        size = [1] * n

        def find(node):
            while node != parents[node]:
                node = parents[node]
            return node


        def union(nod1,node2):
            parent1 = find(node1)
            parent2 = find(node2)

            if size[parent2] > size[parent1]:
                parent1,parent2 = parent2,parent1

            size[parent1] += size[parent2]
            parents[parent2] = parents[parent1]

        for node1,node2 in edges:
            union(node1,node2)

        return find(source) == find(destination)