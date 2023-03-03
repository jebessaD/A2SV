class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_store = Counter({0:1})
        prefix = 0
        ans = 0
        for num in nums:
            prefix += num
            if prefix - goal in prefix_store:
                ans += prefix_store[prefix - goal]
            prefix_store[prefix] += 1
        return ans