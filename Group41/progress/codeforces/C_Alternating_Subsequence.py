n= int(input())
for _ in range(n):
    size = int(input())

    arr = list(map(int,input().split(" ")))
    left = 0
    right = 1
    ans = arr[0]
    while right < size:
        if arr[left] * arr[right] > 0:
            if arr[right] > arr[left]:
                ans += arr[right] - arr[left]
                left = right
                right += 1
            
            else:
                right += 1
     
        else:
            ans += arr[right]
            left = right
            right += 1
      
    print(ans)
