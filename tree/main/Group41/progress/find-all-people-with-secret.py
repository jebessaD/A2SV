class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:

        graph = defaultdict(list)
        for p1,p2,t in meetings:
            graph[p1].append((p2,t))
            graph[p2].append((p1,t))
        
        queue = deque([(firstPerson,0),(0,0)])
        visited = set()
        visited.add((firstPerson,0))
        ans = [0]
        while queue:
            per, time = queue.popleft()
            ans.append(per)
            for child,curr_time in graph[per]:
                if (child,per) not in visited and (per,child) not in visited and curr_time >= time:
                    queue.append((child,curr_time))
                    visited.add((child,per))
                    visited.add((per,child))
        
        return list(set(ans))

            


        