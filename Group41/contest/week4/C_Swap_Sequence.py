size = int(input())
arr = list(map(int,input().split()))
ans=[]
for i in range(len(arr)):
    min_ind = i
    for j in range(i+1,len(arr)):
        if arr[j] < arr[min_ind]:
            min_ind = j
    if min_ind != i:
        arr[i],arr[min_ind] = arr[min_ind],arr[i]
        ans.append((i,min_ind))

print(len(ans))
for res in ans:
    print(*res)
