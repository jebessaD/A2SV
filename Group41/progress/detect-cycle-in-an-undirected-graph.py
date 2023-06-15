from typing import List
from collections import defaultdict
from collections import deque
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    indegrees = defaultdict(int)
	    for i in range(len(adj)):
	        for node in adj[i]:
	            indegrees[node]+= 1
	            
	    queue = deque()          
	    visited = set()
	    for ind in range(V):
	        if not indegrees[ind] or indegrees[ind] == 1:
	            queue.append(ind)
	            visited.add(ind)

	    
	    while queue:
	        parent = queue.popleft()
	        
	        for child in adj[parent]:
	            indegrees[child] -= 1
	            if (not indegrees[child] or indegrees[child] == 1) and child not in visited:
	                queue.append(child)
	                visited.add(child)
	            
	    return not len(visited) == V
