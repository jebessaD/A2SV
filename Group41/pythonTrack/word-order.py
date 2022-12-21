# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
size=input()
arr=[]
for i in range(int(size)):
    arr.append(input())
    
print(len(set(arr)))
frequency = list(Counter(arr).values())
a=list(map(str,frequency))
print(" ".join(a))
