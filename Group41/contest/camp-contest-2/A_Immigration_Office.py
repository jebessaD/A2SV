n = int(input())
names = input().split(" ")

n2 = int(input())
newName = []
for name in range(n2):
    newName.append(input())

for newN in newName:
    left = 0
    right = n - 1
    
    while left <= right  :
        mid = (left + right) // 2
        if newN > names[mid]:
            left = mid + 1
        else:
            right = mid - 1

    print(left )