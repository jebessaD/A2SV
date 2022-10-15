# https://leetcode.com/problems/car-pooling/
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[2],reverse=True)
        total=0
        ans=[0]*trips[0][2]
        for i,j,k in trips:
            for n in range(j-1,k-1):
                ans[n]+=i
                if(ans[n]>capacity):
                    return False
        return True