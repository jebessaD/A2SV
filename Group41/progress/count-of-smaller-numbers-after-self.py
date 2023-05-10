class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans = defaultdict(int)
        nums = [(nums[i],i) for i in range(len(nums))]
        def mergeSort(arr):
            if len(arr) == 1:
                return arr

            mid = len(arr) // 2
        
            left_half = mergeSort(arr[:mid])
            right_half = mergeSort(arr[mid:])

            return merge(arr, left_half,right_half,mid)

        def merge(arr , left_half,right_half,mid):
            arr = []
            i, j = 0, 0
            left_len = len(left_half)
            right_len = len(right_half)
    
            while i < left_len and j < right_len:
                if left_half[i] > right_half[j]:
                    ans[left_half[i]] += right_len - j
                    arr.append(left_half[i])
                    i += 1
                else:
                    arr.append(right_half[j])
                    j += 1
              
            arr += left_half[i:]
            arr += right_half[j:]
            return arr
            
        
        mergeSort(nums)
        res = [ans[num] for num in nums]
        return res