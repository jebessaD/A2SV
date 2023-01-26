class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        right = floor(sqrt(c))
        left = 0
        while left <= right:
            if left**2 + right**2 > c:
                right -= 1
            elif left**2 + right**2 < c:
                left +=1
            else:
                return True
        return False