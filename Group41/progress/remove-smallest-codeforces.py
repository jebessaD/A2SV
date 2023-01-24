size =int(input())
for _ in range(size):
 leng=int(input())-1
 arr= list(map(int,input().split()))
 arr.sort()
 ans="YES"
 for ind in range(leng):
  if arr[ind+1] - arr[ind] > 1:
   ans="NO"
   break
 print(ans)