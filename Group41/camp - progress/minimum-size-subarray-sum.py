class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        size = float("inf")
        curr_sum = 0

        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum >= target :
                size = min(size,right - left + 1)
                curr_sum -= nums[left]
                left += 1

        if size == float("inf"):
            return 0
        return size
        