class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        while n != 0:
            prev = n
            n = n>>1
            if (n + prev) % 2 == 0:
                return False

        return True