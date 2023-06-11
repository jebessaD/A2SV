from typing import List
from collections import defaultdict
from collections import deque


from typing import List


class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        # code here
        indegrees = defaultdict(int)
        graph = defaultdict(list)
        for start,end in edges:
            graph[start].append(end)
            indegrees[end]+=1
            
        queue = deque()
        visited = set()
        ans = [1]*n
        for i in range(1,n+1):
            if not indegrees[i]:
                queue.append((i,1))
                visited.add(i)
                
        while queue:
            parent,level = queue.popleft()
            ans[parent-1] =level
            
            for child in graph[parent]:
                indegrees[child] -= 1
                if not indegrees[child] and child not in visited:
                    queue.append((child,level + 1))
                    visited.add(child)
                    
                    
        res = " ".join(map(str,ans))
        return res
            