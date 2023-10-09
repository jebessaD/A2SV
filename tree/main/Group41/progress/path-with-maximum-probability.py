class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        
        graph = defaultdict(list)
        
        for (start,end),p in zip(edges,succProb):
            graph[start].append((end,-p))
            graph[end].append((start,-p))
            
        probability = {node:0 for node in range(n)}
        visited = set()
        
        queue = []
        queue.append([-1,start_node])
        
        while queue:
            parent_prob,node = heapq.heappop(queue)
            
            if node in visited:
                continue
            
            visited.add(node)
            
            for child,prob in graph[node]:
                curr_prob = - (parent_prob * prob)
                if curr_prob < probability[child]:
                    probability[child] = curr_prob
                    heapq.heappush(queue,[curr_prob,child])
                    
        return -probability[end_node]