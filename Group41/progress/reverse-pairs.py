class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.ans = 0
        def mergeSort(arr):

            if len(arr) == 1:
                return arr
            mid = len(arr) // 2

            left_half = mergeSort(arr[:mid])
            right_half = mergeSort(arr[mid:])

            return merge(left_half,right_half)

        def merge(left_half,right_half):
            arr = []
            i, j ,ptr1 , ptr2 = 0, 0 , 0, 0
            left_len = len(left_half)
            right_len = len(right_half)
            
            while ptr1 < left_len and ptr2 < right_len:

                if left_half[ptr1] > right_half[ptr2] * 2:
                    self.ans += right_len - ptr2
                    ptr1 += 1
                else:
                    ptr2 += 1

            while i < left_len and j < right_len:
                if left_half[i] < right_half[j]:
                    arr.append(right_half[j])
                    j += 1
                else:
                    arr.append(left_half[i])
                    i += 1
              
            arr += left_half[i:]
            arr += right_half[j:]
            return arr
            
        
        mergeSort(nums)
        return self.ans


        