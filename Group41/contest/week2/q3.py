size =int(input())
for _ in range(size):
 input()
 prev=-1
 for i in range(8):
  temp=[]
  for j, char in enumerate(input()):
   if char =="#":
    temp.append(j+1)
    
  if len(temp)==1 and temp[0]==prev:
   print(i+1,temp.pop())
  
  if len(temp) == 2:
   prev=(temp[1]+temp[0])//2