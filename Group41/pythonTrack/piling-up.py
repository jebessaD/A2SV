# Enter your code here. Read input from STDIN. Print output to STDOUT
size=int(input())

for i in range(size):
    left=0
    right=int(input())-1
    blocks=list(map(int,input().split(" ")))
    pile=[]
    ans="Yes"
    while left<right:
        
        if blocks[right]>blocks[left]:
            pile.append(blocks[right])
            right-=1
        else:
            pile.append(blocks[left])
            left+=1
        if pile[-1]<blocks[left] or pile[-1]<blocks[right]:
            ans="No"
            break 
            
    print(ans)
            
        
            
        
    
