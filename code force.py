n,l,r= input().split()
def converter(arr):
    for i,n in enumerate(arr): # [3,1,3]  [ 1,1,1,3,1 1]
        if(arr[-1]==1):
            return arr
        if(n>1):
            break
    return converter((arr[0:i] + [n//2,n%2,n//2] + arr[i+1:len(arr)])[0:int(r)])

print((converter([int(n)])))