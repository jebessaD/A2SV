class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        prefix_sum = 0
        ans = []
        for num in nums:
            prefix_sum += num
            ans.append(prefix_sum)

        return ans