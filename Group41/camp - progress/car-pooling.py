class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        bus_capacity = [0] * (max(map(max, trips)) + 2)

        for passenger,start,end in trips:
            bus_capacity[start] += passenger
            bus_capacity[end] -= passenger

        running_sum = 0
        for num in bus_capacity:
            running_sum += num
            if running_sum > capacity:
                return False

        return True
        