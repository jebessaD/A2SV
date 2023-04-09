n = int(input())

for _ in range(n):
    num = num2 = int(input())
    and_shift = 0

    while num % 2 == 0:
        num = num >> 1
        and_shift += 1

    ans = 1 << and_shift
    
    curr_xor = ans ^ num2

    if not curr_xor:
        if and_shift:
            ans = ans | 1
        else:
            ans = ans | 1 << (and_shift +1)

    print(ans)
    


    





