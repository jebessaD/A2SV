class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        graph = defaultdict(list)
        indegrees = defaultdict(int)
        parents = defaultdict(set)

        for pre,post in prerequisites:
            graph[pre].append(post)
            indegrees[post] += 1

        queue = deque()
        visited = set()
        
        for i in range(numCourses):
            if not indegrees[i]:
                queue.append(i)
                visited.add(i)

        while queue:
            parent = queue.popleft()
            
            for child in graph[parent]:
                indegrees[child] -= 1
                parents[child].add(parent)
                parents[child].update(parents[parent])
                if not indegrees[child]:
                    queue.append(child)
                    visited.add(child)

        ans = []
        for sub1,sub2 in queries:
            ans.append(sub1 in parents[sub2])

        return ans 