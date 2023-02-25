size = int(input())
arr = list(map(int,input().split(" ")))
left = 0
right = len(arr)-1
prefix = [0]
suffix = [0]

for num in arr:
    prefix.append(prefix[-1] + num)

for num in reversed(arr):
    suffix.append(suffix[-1]+num)

left = 0
right = 0
total = prefix[-1]

while True:
    if prefix[left] + suffix[right] == total:
        break

    if prefix[left+1] <= suffix[right + 1]:
        left += 1
    else:
        right += 1

print(left,right)

