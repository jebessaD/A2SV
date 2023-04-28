class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        groups = {}
        graph = defaultdict(list)

        for node1,node2 in dislikes:
            graph[node1].append(node2)
            graph[node2].append(node1)

        visited = set()
        self.ans = True
        def dfs(node,group):
            
            if node in visited:
                return groups[node] == group

            visited.add(node)
            groups[node] = group
            res = True
            for child in graph[node]:
                res = res and dfs(child,not group)
            return res
        for i in range(1,n):
            if i not in visited:
                dfs(i,True)

        return self.ans