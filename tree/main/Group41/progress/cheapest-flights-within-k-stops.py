class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for start,end,price in flights:
            graph[start].append((price,end))

        costs = [float('inf') for i in range(n)]
        parents = [0 for i in range(n)]

        queue = [(0,0,src)]
        while queue:
            stop,price, city = heappop(queue)
            for neigh_price,neighbour in graph[city]:
                curr_price = price + neigh_price
                if curr_price < costs[neighbour] and k >= stop:
                    heappush(queue,(stop+1,curr_price,neighbour))
                    costs[neighbour] = curr_price

        return costs[dst] if costs[dst] !=float('inf') else -1


            



                




        