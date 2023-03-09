
# n,m,k = map(int,input().split(" "))
# matrix = []
# for i in range(n):
#     row = list(input())
#     matrix.append(row)
# ans = 0
# def checkSeat(matrix,ans):
#     for row in matrix:
#         left = 0
#         right = 0
#         while right < len(row):

#             if row[right] == ".":
#                 right += 1
#             else:
#                 right += 1
#                 left = right


#             if right - left >= k:
#                 ans += 1
#     return ans
# ans = checkSeat(matrix,ans)
# matrix = list(zip(*matrix))
# ans = checkSeat(matrix,ans)
# if k == 1:
#     print(ans//2)
# else:
#     print(ans)

n,m,k = map(int,input().split(" "))
matrix = []
for i in range(n):
    row = input().replace(".","0").replace("*","1")
    row = list(map(int,row))
    matrix.append(row)
ans = 0
def checkSeat(matrix,ans):
    for row in matrix:
        left = 0
        right = 0
        while right < len(row):
 
            if row[right] == 0:
                right += 1
            else:
                right += 1
                left = right
 
 
            if right - left >= k:
                ans += 1
    return ans
ans = checkSeat(matrix,ans)
matrix = list(zip(*matrix))
ans = checkSeat(matrix,ans)
if k == 1:
    print(ans//2)
else:
    print(ans)
    