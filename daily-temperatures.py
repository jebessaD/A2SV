class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        order={}
        ans={}
        for i,temp in enumerate(temperatures):
            order[i]=temp
            
        for j in order.keys():
            while(stack and order[stack[-1]]<order[j]):
                index=stack.pop()
                ans[index]=j-index
                
            ans[j]=0
            stack.append(j)
        return(list(ans.values()))