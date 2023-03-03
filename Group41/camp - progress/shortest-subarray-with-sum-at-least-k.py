class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        queue = deque()
        prefix = [0]
        ans = float("inf")

        #find prefix sum
        for num in nums:
            prefix.append(prefix[-1] + num)

        for i,pre in enumerate(prefix):
            
            #monotonic queue 
            while queue and pre <= prefix[queue[-1]]:
                queue.pop()
            #
            while queue and pre - prefix[queue[0]] >= k:
                ind = queue.popleft()
                ans = min(ans, i - ind)
                   
            queue.append(i)

        return -1 if ans == float("inf") else ans