n = int(input())

for _ in range(n):
    arr = list(map(int,input().split(" ")))
    
    pos1= 4 * arr[0]
    pos2= arr[2]*arr[0] + (4 - arr[2]) *arr[1]
    pos3 = 4 * arr[1] + arr[2]*arr[1]

    print(min(pos1,pos2,pos3))