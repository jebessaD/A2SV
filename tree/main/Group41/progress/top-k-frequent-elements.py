class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:		
        
        freq = Counter(nums)
        arr = list(freq.keys())
        k = len(arr) - k
        def quickSort(l,r):
            pivot = freq[arr[r]]
            p = l
            for i in range(l,r):
                if freq[arr[i]] <= pivot:
                    arr[p],arr[i] = arr[i],arr[p]
                    p += 1

            arr[p],arr[r] = arr[r],arr[p]

            if p > k:
                quickSort(l,p-1)
            elif p < k:
                quickSort(p+1,r)
            else:
                return


        quickSort(0,len(arr)-1)
        return arr[k:][::-1]

        
        