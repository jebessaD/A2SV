class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        def distance(x1,y1,x2,y2):
            y = (y2 - y1)**2
            x = (x2 - x1)**2
            return (x + y)**0.5

        graph = defaultdict(set)
        for i,(x1,y1,r1) in enumerate(bombs):
            for j,(x2,y2,r2) in enumerate(bombs):
                if i != j and distance(x1,y1,x2,y2) <= r1:
                    graph[(x1,y1,i)].add((x2,y2,j))

                if i != j and distance(x1,y1,x2,y2) <= r2:
                    graph[(x2,y2,j)].add((x1,y1,i))
                    
        def dfs(node):
            visited.add(node)
            if not node in graph:
                return 
            
            for child in graph[node]:
                if child not in visited :
                    dfs(child)

        max_ = 1
        for node in graph:
            visited = set()
            dfs(node)
            max_ = max(max_,len(visited))

        return max_
