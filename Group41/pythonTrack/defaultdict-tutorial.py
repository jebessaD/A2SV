# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

sizeA,sizeB=input().split(" ")
A_dict=defaultdict(list)
B_dict=defaultdict(list)

for i in range(int(sizeA)):
    A_dict[input()].append(i+1)

for j in range(int(sizeB)):
    b=input()
    if A_dict[b]==[]:
        print("-1")
    else:
        print(" ".join(map(str,A_dict[b])))