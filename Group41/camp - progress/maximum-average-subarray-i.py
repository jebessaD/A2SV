class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = sum(nums[:k])
        left = 0
        max_sum = curr_sum
        for right in range(k,len(nums)):
            curr_sum -= nums[left]
            curr_sum += nums[right]
            max_sum = max( max_sum , curr_sum)
            left += 1

        return max_sum / k
