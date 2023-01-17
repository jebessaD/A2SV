class Solution: 
    def select(self, arr, i):
        # code here 
        minimum=i
        for j in range(i+1,len(arr)):
            if arr[minimum]>arr[j]:
                minimum=j
        return minimum
            
    
    def selectionSort(self, arr,n):
        for k in range(n-1):
            minimum=self.select(arr,k)
            arr[minimum],arr[k]=arr[k],arr[minimum]