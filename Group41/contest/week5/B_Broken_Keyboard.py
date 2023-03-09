from collections import defaultdict
n = int(input())
for _ in range(n):
    store = defaultdict(list)
    arr = input()
    for i,char in enumerate(arr):
        store[char].append(i)
    
    ans = ""
    for key in store:
        for i in range(len(store[key])):
            if len(store[key]) % 2 !=0:
                ans += key
                break
            else:
                if i%2 == 0 and (store[key][i] + 1) != store[key][i+1] :
                    ans += key
                    break

    print("".join(sorted(list(ans))))



