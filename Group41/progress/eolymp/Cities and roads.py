n = int(input())
connected = 0
for _ in range(n):
    connected += sum(map(int,input().split()))

print(connected//2)
