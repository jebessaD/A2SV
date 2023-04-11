class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:

        def isPrime(num):
            if num == 1:
                return False
                
            d = 2
            while d * d <= num:
                if num % d == 0:
                    return False
                d += 1

            return True
        
        ans  = []
        res = []
        min_diff = float("inf")

        for num in range(left,right+1):
            if isPrime(num):
                ans.append(num)

            if len(ans) == 2:
                diff = ans[1] - ans[0]
                if diff < min_diff:
                    min_diff = diff
                    res = [*ans]
                
                if diff == 2:
                    break
                    
                ans = [ans[1]]

        return [-1,-1] if len(res) < 2 else res