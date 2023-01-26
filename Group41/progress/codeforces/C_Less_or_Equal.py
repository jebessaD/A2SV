n,k = map(int,input().split(" "))
nums= list(map(int,input().split(" ")))

nums.sort()
ans = -1
if not( k < n and nums[k] == nums[k-1]) and k!=0:
    ans = nums[k-1]

if k == 0 and min(nums) > 1:
    ans= 1

print(ans)