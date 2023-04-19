class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:

        nodes = defaultdict(set)
        for city1, city2 in roads:
            nodes[city1].add(city2)
            nodes[city2].add(city1)

        max_network = 0
        for city1 in nodes:
            for city2 in nodes:
                isConnected = city1 in nodes[city2] and city1 != city2 
                if city1 != city2 :
                    max_network = max(max_network, len(nodes[city1]) + len(nodes[city2]) - isConnected )

        return max_network

