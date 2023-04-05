from collections import defaultdict 
size = int(input())
for _ in range(size):
    n,m = map(int,input().split(" "))
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int,input().split(" "))))

    left_diagonal = defaultdict(int)
    right_diagonal = defaultdict(int)
    for i in range(n):
        for j in range(m):
            left_diagonal[i+j] += matrix[i][j]
            right_diagonal[i -j] += matrix[i][j]

    max_num = 0
    for row in range(n):
        for col in range(m):
            num = left_diagonal[row+col] + right_diagonal[row-col] - matrix[row][col]
            max_num = max(max_num,num)

    print(max_num)


    