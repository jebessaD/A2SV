class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)
        def eatingSpeed(mid):
            return sum([ math.ceil(pile/mid) for pile in piles])

        while left <= right:
            mid = left + (right - left)//2

            if eatingSpeed(mid) <= h:
                right = mid  - 1
            else:
                left = mid + 1

        return left