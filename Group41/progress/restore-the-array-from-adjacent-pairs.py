class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegrees = defaultdict(int)
        for node1,node2 in adjacentPairs:
            graph[node1].append(node2)
            graph[node2].append(node1)
            indegrees[node1] += 1
            indegrees[node2] += 1
        
        visited = set()
        ans = []
        def dfs(node):
            visited.add(node)
            ans.append(node)
            for child in graph[node]:
                if child not in visited:
                    dfs(child)

        for node in indegrees:
            if indegrees[node] == 1:
                dfs(node)
                break

        return ans


