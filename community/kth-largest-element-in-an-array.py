class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]


#solution 2 using heap
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums=list(map(lambda x:-x,nums))
        heapq.heapify(nums)
        for i in range(k-1):
            heapq.heappop(nums)
        return -heapq.heappop(nums)
        