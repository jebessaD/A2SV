from collections import defaultdict
node_len = int(input())
operations = int(input())
nodes = defaultdict(list)
for _ in range(operations):
    arr = list(map(int,input().split()))
    if arr[0] == 1:
        nodes[arr[1]].append(arr[2])
        nodes[arr[2]].append(arr[1])
    elif arr[0] == 2:
        print(*nodes[arr[1]])
