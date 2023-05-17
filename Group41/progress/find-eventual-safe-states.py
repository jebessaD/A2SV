class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        outgoing = [0]*len(graph)
        reverse_graph = defaultdict(list)
        for i in range(len(graph)):
            outgoing[i] = len(graph[i])
            for node in graph[i]:
                reverse_graph[node].append(i)

        queue = deque()
        visited = set()
        for i in range(len(graph)):
            if not outgoing[i]:
                queue.append(i)
                visited.add(i)

        ans = []
        while queue:
            parent = queue.popleft()
            if not outgoing[parent]:
                ans.append(parent)

            for child in reverse_graph[parent]:
                outgoing[child]-=1
                if not outgoing[child] and child not in visited:
                    queue.append(child)
                    visited.add(child)

        return sorted(ans)




