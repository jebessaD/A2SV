n,k = map(int,input().split(" "))
nums= list(map(int,input().split(" ")))

nums.sort()
maximum = nums[k-1]
if k < n and nums[k] == maximum:
    print(-1)
else:
    print(maximum)