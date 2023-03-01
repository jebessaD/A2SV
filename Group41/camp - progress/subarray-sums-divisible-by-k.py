class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = 0
        ans = 0
        remainder_store = {0:1}

        for num in nums:
            prefix += num
            if prefix % k in remainder_store:
                ans += remainder_store[prefix % k]
            remainder_store[prefix % k] = remainder_store.get(prefix % k,0) + 1

        return ans
        