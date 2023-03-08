class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        if n == 1:
            return 0
                
        bit = self.kthGrammar( n-1, (k + 1) //2)
        
        if k % 2 == 0:
            bit = 1 - bit

        return bit