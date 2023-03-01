n = int(input())

teachers = list(map(int,input().split(" ")))
students = list(map(int,input().split(" ")))

difference = []
for t_unit , s_unit in zip(teachers,students):
    difference.append(t_unit - s_unit)
difference.sort()
left = 0
right = n-1
ans = 0

while left < right:
    if difference[right] + difference[left] > 0:
        ans += right - left
        right -= 1
    else:
        left += 1

print(ans)