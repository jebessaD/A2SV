# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m= input().split()
arr= input().split()
A=set(input().split())
B=set(input().split())
happiness=0
for num in arr:
    if num in A:
        happiness+=1
    elif num in B:
        happiness-=1
        
print(happiness)