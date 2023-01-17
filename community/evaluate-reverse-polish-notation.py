class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # operator={'+':+,'-':-,'*':*,'/'://}
        operator={"+", "-", "*", "/"}
        stack=[]
        for num in tokens:
            if num in operator:     
                a=int(stack.pop())
                b=int(stack.pop())
                if num=="+":
                    stack.append(b+a)
                elif num=="*":
                    stack.append(b*a)
                elif num=="-":
                    stack.append(b-a)
                else:
                    stack.append(int(b/a))
            else:
                stack.append(num)
        return stack.pop()
        