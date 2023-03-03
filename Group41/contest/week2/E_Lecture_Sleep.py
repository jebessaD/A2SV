n , size = map(int, input().split(" "))
arr = list(map(int,input().split(" ")))
awake = list(map(int,input().split(" ")))
total = sum( [ x * y for x,y in zip(arr,awake)])
nums = list (map(lambda x: 0 if x == 1 else 1,awake ))
zero_values = [ x * y for x,y in zip(arr,nums)]
ans = sum(zero_values[:size])
max_ans = ans
left = 0
right = size

while right < len(zero_values):
    ans -= zero_values[left]
    ans += zero_values[right]
    left += 1
    right += 1
    max_ans = max( ans, max_ans)

print(max_ans + total)
