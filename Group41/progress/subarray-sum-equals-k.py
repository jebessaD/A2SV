class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = ans = 0
        prefix_freq = {0:1}

        for num in nums:
            prefix += num
            if prefix - k in prefix_freq:
                ans += prefix_freq[prefix - k]
            prefix_freq[prefix] = prefix_freq.get(prefix,0) + 1
            
        return ans
        