class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for bracket in s:
            if bracket == "(":
                stack.append("(")

            elif bracket==")" and stack[-1] == "(" :
                stack.pop()
                if stack and stack[-1] != "(":
                    stack[-1] += 1
                else:
                    stack.append(1)
            else:
                poped = 0
                num = 0
                while poped != "(" and stack:
                    num = num * 10 + int(poped)
                    poped = stack.pop()
                
                if stack and stack[-1] != "(":
                    stack[-1] += num * 2
                else:
                    stack.append(num*2)
      
        return sum(stack)