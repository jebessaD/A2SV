class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        nodes = defaultdict(list)
        n = len(isConnected)

        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    nodes[i+1].append(j+1)
        visited = set()
        
        def dfs(city):
            visited.add(city)

            for node in nodes[city]:
                if node not in visited:
                    dfs(node)

        ans = 0
        for city in range(1,n+1):
            if city not in visited:
                ans += 1
                dfs(city)
       
        return ans
        