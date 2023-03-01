class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator={"+", "-", "*", "/"}
        for char in tokens:
            if char not in operator:
                stack.append(int(char))
            else:
                num= stack.pop()
                if char == "+":
                    stack[-1] += num
                elif char == "*":
                    stack[-1] *= num
                elif char == "-":
                    stack[-1] -= num
                else:
                    stack[-1] = int(stack[-1] / num)

        return stack.pop()
