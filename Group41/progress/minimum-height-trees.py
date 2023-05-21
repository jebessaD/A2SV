class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]

        indegrees = defaultdict(int)
        graph = defaultdict(list)

        for node1 ,node2 in edges:
            graph[node2].append(node1)
            graph[node1].append(node2)
            indegrees[node1] += 1
            indegrees[node2] += 1
        
        queue = deque()
        visited = set()
        
        for i in indegrees:
            if indegrees[i] == 1:
                queue.append((i,0))
                visited.add(i)

        ans = defaultdict(list)
        while queue:
            parent,level = queue.popleft()
            ans[level].append(parent)
            for child in graph[parent]:
                indegrees[child] -= 1
                if child not in visited and indegrees[child] == 1:
                    visited.add(child)
                    queue.append((child,level + 1))

        max_level = max(ans.keys())
        return ans[max_level]