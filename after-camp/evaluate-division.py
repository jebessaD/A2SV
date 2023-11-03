class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = defaultdict(list)

        for (x,y),val in zip(equations,values):
            graph[x].append((y,val))
            graph[y].append((x,1/val))

        def find_division(start,end):
            if start not in graph or end not in graph:
                return -1
            queue = deque()
            queue.append((1,start))
            visited = set()

            while queue:
                curr_res,node = queue.popleft()
                if node == end:
                    return curr_res
                visited.add(node)
                for child,val in graph[node]:
                    if child not in visited:
                        queue.append((curr_res*val,child))

            return -1

        return [find_division(start,end) for start,end in queries ]

                

        