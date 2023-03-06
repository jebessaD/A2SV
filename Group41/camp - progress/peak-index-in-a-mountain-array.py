class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        right = len(arr) - 1
        left = 0

        while left <= right:
            mid = left + (right - left)//2
            
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1

        return left