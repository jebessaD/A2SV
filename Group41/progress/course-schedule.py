class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)
        indegrees = [0]*numCourses

        for post,pre in prerequisites:
            graph[pre].append(post)
            indegrees[post] += 1

        queue = deque()
        visited = set()

        for i,indegree in enumerate(indegrees):
            if indegree == 0:
                visited.add(i)
                queue.append(i)

        while queue:
            parent = queue.popleft()

            for child in graph[parent]:
                indegrees[child] -= 1
                if indegrees[child] == 0 and child not in visited:
                    visited.add(child)
                    queue.append(child)

        return len(visited) == numCourses