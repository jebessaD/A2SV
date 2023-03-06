class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:

        prefix = [0]* (len(nums) +1)

        for start,end in requests:
            prefix[start] += 1
            prefix[end + 1] -= 1

        for i in range(1,len(prefix)):
            prefix[i] += prefix[i-1]
        prefix.pop()

        nums.sort()
        prefix.sort()
        ans = 0
        for num , pre in zip(nums,prefix):
            ans += (num * pre)

        return ans % (10**9 + 7)