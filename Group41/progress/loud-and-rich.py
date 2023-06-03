class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:

        outgoings = defaultdict(int)
        graph = defaultdict(list)

        for pr1,pr2 in richer:
            graph[pr1].append(pr2)
            outgoings[pr2] += 1

        queue = deque()
        visited = set()
        ans = []
        for i in range(len(quiet)):
            ans.append(i)
            if not outgoings[i]:
                queue.append(i)
                visited.add(i)

        while queue:
            parent = queue.popleft()

            for child in graph[parent]:
                
                if quiet[ans[child]] > quiet[ans[parent]]:
                    ans[child] = ans[parent]

                outgoings[child] -= 1
                if not outgoings[child] and child not in visited:
                    queue.append(child)
                    visited.add(child)

                
        return ans
