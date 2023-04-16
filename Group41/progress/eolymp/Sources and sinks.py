n = int(input())
source= set([ i + 1 for i in range(n)])
sink = []
for i in range(n):
    arr = list(map(int,input().split(" ")))
    if not any(arr):
        sink.append(i + 1)

    for j in range(n):
        if arr[j] == 1:
            source.discard(j+1)
        
print(len(source), *source)
print(len(sink), *sink)