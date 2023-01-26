class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        size = len(arr)
        ans=[]

        while size > 0:
            if sorted(arr)==arr:
                return ans
                
            ind = arr.index(size)
            ans.append(ind+1)
            arr[:ind+1]= reversed(arr[:ind+1])
            arr[:size]= reversed(arr[:size])
            ans.append(size)
            size -= 1
        return ans
            