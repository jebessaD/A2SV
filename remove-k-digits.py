class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        if(len(num)==k):
            return "0"
        for n in num:
            while(stack and k>0 and (stack[-1] > n)):
                stack.pop()
                k-=1
            stack.append(n)
        ans = ''.join(map(str, stack))
        
        if(k !=0):
            return(str(int(ans[:-k])))
        return(str(int(ans)))

