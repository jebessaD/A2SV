size = int(input())
nums = list(map(int,input().split(" ")))
left =0
right = size - 1

inx=0
ans=[0,0]
while left <= right:

    if nums[left] > nums[right]:
        ans[ inx%2 ] += nums[left]
        left += 1
    else:
        ans[ inx%2 ] += nums[right]
        right -=1

    inx+=1

print(*ans)

