class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count = 0
        for n in range(1,k + len(arr)+1):
            if n not in arr:
                count += 1
            
            if count == k:
                return n

        