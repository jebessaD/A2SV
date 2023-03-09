class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        def divider(mid):
            return sum([ math.ceil(n/mid) for n in nums])

        while left <= right:
            mid = left + (right - left)//2

            if divider(mid) <= threshold:
                right = mid - 1
            else:
                left = mid + 1
                
        return left
        