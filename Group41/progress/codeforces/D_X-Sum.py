size = int(input())
for _ in range(size):
    matrix = []
    n,m= map(int,input().split(" "))
    row = []
    for z in range(n):
        row = list(map(int,input().split(" ")))
        matrix.append(row)
    
    def sumDiagonals(matrix,i,j):
        dec_value = min(i,j)
        start = [i-dec_value , j-dec_value]
        res = 0
        while start[0] < len(matrix) and start[1] < len(matrix[0]):
            res +=  matrix[start[0]][start[1]]
            start[0] += 1
            start[1] += 1

        return res - matrix[i][j]
        

    diagonal_sum = {}
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if (col + row) in diagonal_sum:
                diagonal_sum[row + col] += matrix[row][col]
            else:
                diagonal_sum[row + col] = matrix[row][col]
    ans = 0
    output = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
           temp = sumDiagonals(matrix,row,col)
           output = temp + diagonal_sum[row + col]
           ans  = max(ans, output) 


    print(ans)

            