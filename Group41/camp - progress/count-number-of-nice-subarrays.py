class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = list(map(lambda x : x%2 ,nums))
        prefix = 0
        ans = 0
        prefix_store = {0:1}
        for num in nums:
            prefix += num
            if prefix - k in prefix_store:
                ans += prefix_store[prefix-k]
            prefix_store[prefix] = prefix_store.get( prefix, 0)+1
        return ans