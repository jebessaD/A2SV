n = int(input())
for _ in range(n):
    arr = list(input())
    left = right = 0
    store = {}
    left = 0
    ans = float("inf")
    for right in range(len(arr)):
        store[arr[right]] = store.get(arr[right],0) + 1

        while len(store)==3:
            ans = min(ans,right - left + 1)
            store[arr[left]] -= 1
            if store[arr[left]]==0:
                store.pop(arr[left])
            left += 1
    if ans == float("inf"):
        print("0")
    else:
        print(ans)

