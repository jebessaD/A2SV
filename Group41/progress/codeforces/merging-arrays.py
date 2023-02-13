n,m =map(int,input().split(" "))
arr1=list(map(int,input().split(" ")))
arr2=list(map(int,input().split(" ")))
 
ptr1=ptr2=0
ans=[]
while ptr1 < n or ptr2 < m:
 
 if ptr1 >= n:
  ans.append(arr2[ptr2])
  ptr2 +=1
  continue
 elif ptr2 >= m:
  ans.append(arr1[ptr1])
  ptr1 += 1
  continue
 
 if arr1[ptr1] < arr2[ptr2]:
  ans.append(arr1[ptr1])
  ptr1 += 1
 else:
  ans.append(arr2[ptr2])
  ptr2 +=1
  
print(" ".join(map(str,ans)))