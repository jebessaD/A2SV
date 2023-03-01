size = int(input())
arr = list(map(int,input().split(" ")))

dist=0
ans = 0
for i in range(len(arr)-1):
    if arr[i] <= arr[i+1]:
        dist += 1
        ans = max(ans, dist)
        # print(dist,i)
    else:
        dist = 0
        
print(ans+1)
