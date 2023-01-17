class Solution:
    def decodeString(self, s: str) -> str:
        element,sub,stack=0,"",[]
        
        for i in s:
            while(i=="]"):
                a=stack.pop()
                if(a=="["):
                    num=stack.pop()
                    stack.append(num*sub)
                    sub=""
                    break
                else:
                    sub=a + sub
                    
            if i.isnumeric() :
                element=element * 10 + int(i)
            elif(i=="["):
                stack.append(element)
                stack.append(i)
                element=0
            elif(i !="]"):
                stack.append(i)
                
        return(''.join(stack))


            
                