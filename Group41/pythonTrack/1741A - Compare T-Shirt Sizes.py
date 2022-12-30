size= int(input())
 
for i in range(size):
 str1,str2=input().split(" ")
 order={"S":0,"M":1,"L":2}
 
 if order[str1[-1]] > order[str2[-1]]:
  print(">")
 elif order[str1[-1]] < order[str2[-1]]:
  print("<")
 else:
  if str1[-1]=="S":
   if len(str1)>len(str2):
    print("<")
   elif len(str1) < len(str2):
    print(">")
   else:
    print("=")
  else:
   if len(str1)<len(str2):
    print("<")
   elif len(str1) > len(str2):
    print(">")
   else:
    print("=")