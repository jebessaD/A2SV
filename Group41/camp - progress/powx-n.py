class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            x = 1 / x
            n = -n

        if n % 2 != 0:
            return self.myPow(x, n-1) * x
        
        x = x ** 2
        n //= 2
        return self.myPow(x, n)
        