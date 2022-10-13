class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words=Counter(sorted(words)).most_common()
        return list(map(lambda x:x[0],words[:k]))   