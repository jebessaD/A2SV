size = int(input())
arr = list(map(int,input().split()))
neg = []
zero = []
pos = []
for num in arr:
    if num > 0:
        pos.append(num)
    elif num < 0:
        neg.append(num)
    else:
        zero.append(num)
neg_pop = "a"
zero_swap = len(zero)
pos_swap = sum(pos)-len(pos)
if len(neg)%2!=0 and len(zero)==0:
    pos_swap+=2

neg_swap = - (sum(neg) + len(neg))


print(zero_swap+pos_swap+ neg_swap)


