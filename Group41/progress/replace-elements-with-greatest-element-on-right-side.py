class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        max_to_right=-1
        for ind in range(len(arr)-1,-1,-1):
            temp=arr[ind]
            arr[ind]=max_to_right
            max_to_right = max(temp,max_to_right)

        return arr
            