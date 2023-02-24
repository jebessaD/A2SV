size = int(input())
for _ in range(size):
    n = int(input())
    arr = list(map(int,input().split(" ")))
    ans = []
    left = 0
    right = n-1


    while left < right :
        ans.append(arr[left])
        left +=1
        ans.append(arr[right])
        # left += 1
        right -= 1
    
    if n%2 != 0:
        ans.append(arr[left])


    print(*ans)
