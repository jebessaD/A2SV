class Solution:
    def myPow(self, x: float, n: int) -> float:
        # print(x,n)
        if(n==1 or x==0):
            return x
        
        elif(n<0):
            x=1/x
            n = -n
        elif(n==0):
            return 1
        
        if(n%2==0):
            x *=x
            n //=2
            return self.myPow(x,n)
        else:
            # if()
            c=x
            x *=x
            n //=2
            return self.myPow(x,n) * c

        