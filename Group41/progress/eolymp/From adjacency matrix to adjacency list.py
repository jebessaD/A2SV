n = int(input())

for i in range(n):
    arr = list(map(int,input().split()))
    ans = []
    for j in range(len(arr)):
        if arr[j]:
            ans.append(j + 1)
    
    print(len(ans), *ans)
