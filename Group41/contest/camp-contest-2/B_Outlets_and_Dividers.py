n = int(input())
for _ in range(n):
    stu , m = map(int,input().split(" "))
    arr = list(map(int,input().split(" ")))
    arr.sort()
    arr = list(reversed(arr))
    outlate = 2
    ans = -1
    for i,num in enumerate(arr):
        if outlate >= stu:
            ans = i
            break
        else:
            outlate = outlate + num - 1

    if ans == -1 and outlate >= stu:
        ans = i + 1

    print(ans)