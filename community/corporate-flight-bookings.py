# https://leetcode.com/problems/corporate-flight-bookings/submissions/
# prefix sum approach

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        plane=[0]*(n+1)
        for i,j,seats in bookings:
            plane[i-1] +=seats
            plane[j] -=seats
        plane.pop()
        presum,ans=0,[]
        for num in plane:
            presum+=num
            ans.append(presum)
        return ans