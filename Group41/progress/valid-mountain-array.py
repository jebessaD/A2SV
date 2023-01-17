class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

        ind=0
        to_pick = to_valley = False
        while ind < len(arr)-1 and arr[ind] < arr[ind+1]:
            to_pick = True
            ind += 1

        while ind < len(arr)-1 and arr[ind] > arr[ind + 1]:
            to_valley = True
            ind +=1
            
        if to_pick and to_valley and len(arr) == ind+1:
            return True