class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:      
        time_to_complete = []
        for s,v in zip(position,speed):
            time_to_complete.append((s,(target - s) / v))
        
        time_to_complete.sort()
        monotonic_stack = []
        for _,time in time_to_complete: 
            while monotonic_stack and monotonic_stack[-1] <= time:
                monotonic_stack.pop()

            monotonic_stack.append(time)

        return len(monotonic_stack)