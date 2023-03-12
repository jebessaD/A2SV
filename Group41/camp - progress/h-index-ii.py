class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        right = len(citations) - 1
        length = len(citations)

        while left <= right:
            mid = left + (right - left)//2
            if citations[mid] < length - mid:
                left = mid + 1
            else:
                right = mid - 1

        return length - left
        