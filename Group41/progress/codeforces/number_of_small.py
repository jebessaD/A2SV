input()
arr1=list(map(int,input().split(" ")))
arr2=list(map(int,input().split(" ")))
ptr1 = ptr2 = count = 0
ans=[]
while ptr2 < len(arr2):
 
 if ptr1 < len(arr1) and arr1[ptr1] < arr2[ptr2]:
  count+=1
  ptr1+=1
 else:
  ans.append(count)
  ptr2+=1
print(*ans)

# https://codeforces.com/edu/course/2/lesson/9/1/practice/status