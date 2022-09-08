class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        p1=0
        p2=0
        stack=[]
        for i in range(len(pushed)):
            stack.append(pushed[p1])
            p1+=1
            while(stack and (stack[-1]==popped[p2])):
                stack.pop()
                p2+=1
        
        if(stack):
            return False
        return True
            
            
            