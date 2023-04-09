class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:

        prime_divisors = set()

        def findPrimeDivisor(num):         
            d = 2
            while d * d <= num:
                while num % d == 0:
                    prime_divisors.add(d)
                    num //= d
                d += 1

            if num > 1:
                prime_divisors.add(num)

        for num in nums:
            findPrimeDivisor(num)

        return len(prime_divisors)
