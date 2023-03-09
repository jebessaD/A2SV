size = int(input())
for _ in range(size):
    n,m,k = map(int,input().split(" "))
    arr1 = sorted(list(input()))
    arr2 = sorted(list(input()))
    ans = []
    ptr1 = 0
    ptr2 = 0
    count1 = 0
    count2 = 0
    while ptr1 < n and ptr2 < m:
        if (count1 < k and arr1[ptr1] < arr2[ptr2]) or count2 >= k:
            ans.append(arr1[ptr1])
            ptr1 += 1
            count1 += 1
            count2 = 0
        else:
            count1 = 0
            ans.append(arr2[ptr2])
            count2 += 1
            ptr2+=1

    print("".join(ans))
