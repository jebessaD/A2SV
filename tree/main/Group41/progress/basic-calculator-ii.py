class Solution:
    def calculate(self, s: str) -> int:
        stack,opp, num=[],"+",0
        s=s.replace(" ","")
        for i,n in enumerate(s):
            if (n.isnumeric()):
                num= num*10 + int(n)
            if(not n.isnumeric() or i==len(s)-1):
                if(opp=="+"):
                    stack.append(num)
                elif(opp=="-"):
                    stack.append(-num)
                elif(opp=="*"):
                    a=stack.pop()
                    stack.append(a*num)
                elif(opp=="/"):
                    a=stack.pop()
                    stack.append(int(a/num))
                opp=n
                num=0
                    
                
        return sum(stack)