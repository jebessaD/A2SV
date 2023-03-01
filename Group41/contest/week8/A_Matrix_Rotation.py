size = int(input())
for _ in range(size):

    def checkBeuty(matrix):
        
        top_left = matrix[0][0]
        bottom_left = matrix[1][0]
        top_right = matrix[0][1]
        bottom_right = matrix[1][1]

        if top_left < top_right and bottom_left < bottom_right and top_left < bottom_left  and top_right < bottom_right:
            return True
        return False
    
    def rotateAndCheck():
        matrix = []
        ans = "NO"
        for _ in range(2):
            row = list(map(int,input().split(" ")))
            matrix.append(row)
        for i in range(4):
            res = checkBeuty(matrix)
            if res:
                ans = "YES"
                break 
            matrix = [[matrix[1][0],matrix[0][0]],[matrix[1][1],matrix[0][1]]]

        print(ans)

    rotateAndCheck()
