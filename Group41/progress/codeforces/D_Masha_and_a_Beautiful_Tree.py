n = int(input())

for _ in range(n):
    num = int(input())
    arr = list(map(int,input().split(" ")))
    count = 0
    def solve(arr):
        global count
        if len(arr) == 1:
            return arr
        
        mid = len(arr)//2
        sol1 = solve(arr[:mid])
        sol2 = solve(arr[mid:])

        if sol1[0] > sol2[0]:
            count += 1
            return sol2 + sol1
        return sol1 + sol2
    
    new_arr= solve(arr)

    if new_arr == sorted(arr):
        print(count)
    else:
        print(-1)

    count = 0
