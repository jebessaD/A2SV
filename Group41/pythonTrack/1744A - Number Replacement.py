size= int(input())

for i in range(size):
 input()
 arr=input().split(" ")
 string=input()
 store={}
 ans="YES"
 for num,char in zip(arr,string):
  if num in store:
   if store[num] != char:
    ans="NO"
  else:
   store[num]=char
   
 print(ans)

