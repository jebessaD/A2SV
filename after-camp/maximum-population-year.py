class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        logs.sort()
        store = defaultdict(int)
        ans = logs[0][0]
        for i in range(len(logs)-1):
            if logs[i+1][0] < logs[i][1] :
                for year in range(logs[i+1][0],logs[i][1]):
                    store[year] += 1

        sorted_dict = sorted(store.items(), key=lambda item: (-item[1], item[0]))
        if sorted_dict and sorted_dict[0][1]:
            return sorted_dict[0][0]
        return ans

        