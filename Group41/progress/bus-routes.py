class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        for i,route in enumerate(routes):
            routes[i] = set(route)

        queue = deque()
        visited = set()

        queue.append((source,0))
                
        while queue:

            parent,level = queue.popleft()
            if parent == target:
                return level

            for i,route in enumerate(routes):
                
                if i not in visited and parent in route:
                    visited.add(i)
                    for r in route:
                        queue.append((r,level+1))
                
        return -1