size = int(input())
arr = list(map(int,input().split(" ")))
arr.sort()
ans = 0
left = 0

for right in range(len(arr)):
    while arr[right] - arr[left] > 5:
        left += 1
    ans = max(ans,right - left + 1)

print(ans)