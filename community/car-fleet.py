class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        data={}
        stack=[]
        for i in range(len(speed)):
            data[position[i]]=(target-position[i])/speed[i]   
        sorted_data=dict(sorted(data.items()))
        # print(sorted_data)
        for i in sorted_data.keys():
            while(stack and stack[-1]<=data[i]):
                stack.pop()
            stack.append(data[i])
        return(len(stack))