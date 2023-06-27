from collections import defaultdict
from collections import deque
def parallelCourses(n, prerequisites):
    # Write your code here.
    graph = defaultdict(list)
    indegrees = defaultdict(int)
    for pre,post in prerequisites:
        graph[pre].append(post)
        indegrees[post] += 1


    queue = deque()
    visited = set()
    for i in range(1,n+1):
        if i not in indegrees:
            queue.append((i,1))
            visited.add(i)
    max_level = -1

    while queue:
        parent, level = queue.popleft()
        
        max_level = max(max_level,level)
        for child in graph[parent]:
            indegrees[child] -= 1
            if not indegrees[child]:
                queue.append((child,level+1))
                visited.add(child)

    if len(visited) != n:
        return -1
    return max_level
