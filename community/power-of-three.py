import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def divider(n):
            if(math.isclose(n,1,rel_tol=1e-20)):
                return True
            elif(n<1):
                return False 
            return divider(n/3)
        return divider(n)
        