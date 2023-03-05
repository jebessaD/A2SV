size = int(input())
for _ in range(size):
    leng , iter = map(int,input().split(" "))
    prefix = [float("inf")]
    postfix = [float("inf")]
    arr = list(map(int,input()))
    for i in range(len(arr)):
        if arr[i] == 1:
            prefix.append(0)
        else:
            prefix.append(prefix[-1]+1)

        if arr[~i] == 1:
            postfix.append(0)
        else:
            postfix.append(postfix[-1]+1)
                
    prefix.pop(0)
    postfix.reverse()
    postfix.pop()
    
    for (i,(pre_dist,post_dist)) in enumerate(zip(prefix,postfix)):
        if min(pre_dist,post_dist) <= iter and pre_dist!= post_dist:
            arr[i] = 1

    print("".join(map(str,arr)))
