class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        parents = list(range(len(edges)+1))
        size = [1] * (len(edges) + 1)
      
        def find(node):
            root = node
            while parents[root] != root:
                root = parents[root]

            while parents[node] != node:
                temp = parents[node]
                parents[node] = root
                node = temp
            return root

        def union(node1,node2):
            parent1 = find(node1)
            parent2 = find(node2)
            if parent1 == parent2:
                return [node1,node2]
            
            if size[parent1] < size[parent2]:
                parent1,parent2 = parent2,parent

            size[parent1] += size[parent2]
            parents[parent2] = parents[parent1]

        for x,y in edges:
            res = union(x,y)
            if res:
                return res
            
            

