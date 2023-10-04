class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)
        distances = {node:float('inf') for node in range(1,n+1)}

        for start,end,weight in times:
            graph[start].append((end,weight))

        distances[k] = 0
        queue = [(0,k)]
        visited = set()
        
        while queue:
            curr_dist, curr_node = heapq.heappop(queue)
            if curr_node in visited:
                continue
            visited.add(curr_node)

            for child, weight in graph[curr_node]:
                distance = curr_dist + weight
              
                if distance < distances[child]:
                    distances[child] = distance
                    heapq.heappush(queue,(distance,child))

        return -1 if max(distances.values()) == float('inf' ) else max(distances.values())
        