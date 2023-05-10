class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        frequency = defaultdict(int)
        for word in words:
            frequency[word] += 1

        arr = list = [(-v, k) for k, v in frequency.items()]

        heapq.heapify(arr)
        ans = []
        for i in range(k):
            _,word = heappop(arr)
            ans.append(word)

        return ans