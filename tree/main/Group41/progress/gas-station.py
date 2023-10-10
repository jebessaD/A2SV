class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        nums = [g - c for g,c in zip(gas,cost)]
        n = len(nums)
        if sum(nums) < 0:
            return -1
        curr_gas = 0
        start = 0
        for j in range(n):
            curr_gas += nums[j]
            if curr_gas < 0:
                curr_gas = 0
                start = j + 1

        return start
        