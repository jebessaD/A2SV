size = int(input())
for _ in range(size):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(input())
    store = set(arr)
    ans = []
    for word in arr:
        res = "0"
        for i in range(len(word)):
            s1= word[:i+1]
            s2 = word[i+1:]
            if s1 in store and s2 in store:
                res = "1"
                break
        ans.append(res)
            

    print("".join(ans))
            