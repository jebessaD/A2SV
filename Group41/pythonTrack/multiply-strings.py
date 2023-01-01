class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res=0
        for i,m in enumerate(reversed(num2)):
            ans=0
            for j,n in enumerate(reversed(num1)):
                temp = (ord(m)-48 )*(ord(n)-48 )
                ans= ans + (temp * 10**j)
            res=(res+ ans*(10**(i)))
        return str(res)