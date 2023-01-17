import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if(math.isclose(n,1,rel_tol=1e-20)):#to compare float.. if (n==1)
            return True
        elif(n<1):
            return False 
        return self.isPowerOfFour(n/4)
