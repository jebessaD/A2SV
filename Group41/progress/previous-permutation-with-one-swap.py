class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1,0,-1):
            if arr[i-1] > arr[i]:
                nearest_min = i
                j = i
                while j < len(arr) and arr[j] < arr[i-1]:
                    if arr[j] > arr[nearest_min]:
                        nearest_min = j
                    j += 1

                arr[nearest_min],arr[i-1] = arr[i-1],arr[nearest_min]
                
                break

        return arr
        