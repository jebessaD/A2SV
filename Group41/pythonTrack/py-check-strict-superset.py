# Enter your code here. Read input from STDIN. Print output to STDOUT

A=set(input().split(" "))
size = int(input())
ans=True
for i in range(size):
    new_set=set(input().split(" "))
    if not new_set.issubset(A) or len(A) <= len(new_set):
        ans=False
        break
    
print(ans)
    