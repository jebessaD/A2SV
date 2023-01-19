size =int(input())
arr = list(map(int,input().split(" ")))
neg=[]
pos = []
zero = []

for num in arr:
 if num == 0:
  zero.append(num)
 elif num > 0:
  pos.append(num)
 else:
  neg.append(num)
  
if len(neg) % 2 ==0:
 negative = neg.pop()
 zero.append(negative)
 
if len(pos) == 0:
 first=neg.pop()
 second=neg.pop()
 pos.append(first)
 pos.append(second)
print(len(neg)," ".join(list(map(str,neg))))
print(len(pos)," ".join(list(map(str,pos))))
print(len(zero)," ".join(list(map(str,zero))))
