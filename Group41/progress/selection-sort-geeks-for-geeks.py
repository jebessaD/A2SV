class Solution: 
    def select(self, arr, i):
        # code here 
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        return min_index
    
    def selectionSort(self, arr,n):
        for i in range(len(arr)):
            ind = self.select(arr,i)
            arr[ind],arr[i] = arr[i],arr[ind]