class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        indegrees = [0] * n
        ans = [[] for i in range(n)]
        print(ans)
        graph = defaultdict(list)
        for start,end in edges:
            graph[start].append(end)
            indegrees[end] += 1

        print(indegrees,graph)
        queue = deque()
        visited = set()
        for i in range(n):
            if not indegrees[i]:
                queue.append(i)
                visited.add(i)

        while queue:
            parent = queue.popleft()
            
            for child in graph[parent]:
                indegrees[child] -= 1
                ans[child].append(parent)
                ans[child].extend(ans[parent])
                ans[child] = sorted(list(set(ans[child])))

                if not indegrees[child] and child not in visited:
                    queue.append(child)
                    visited.add(child)

        return ans
