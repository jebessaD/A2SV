class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        target = len(graph) - 1
        ans = []
        def dfs(node,candidate):

            if node == target:
                ans.append(candidate[:])
            
            for curr in graph[node]:
                candidate.append(curr)
                dfs(curr,candidate)
                candidate.pop()

        dfs(0,[0])
        return ans
        