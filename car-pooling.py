# https://leetcode.com/problems/car-pooling/


#first solution using brute force
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

# second and optimal solution using prefix sum
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[2], reverse=True) # sort by index ==2 to get last destination
        car=[0]*(trips[0][2] + 1)  #get last destination for second index

        for n,i,j in trips:   #add n number of person at index i and drop person at index of j
            car[i] +=n
            car[j] -=n
            
        total=0
        for person in car:
            total+=person
            if total>capacity: return False
        return True
        