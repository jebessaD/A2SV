class Solution:
    def isValid(self, s: str) -> bool:
        data={'(': ')', '{': '}', '[':']'}
        stack=[]
        for brac in s:
            if brac in data.keys():
                stack.append(brac)
            else:
                if len(stack)>0:
                    a= stack.pop()
                    if data[a] != brac:
                        return False
                else:
                    return False
        if len(stack)==0:
            return True
