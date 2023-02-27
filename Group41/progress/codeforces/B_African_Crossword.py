from collections import Counter
n, m  = map(int,input().split(" "))
matrix = []

for _ in range(n):
     matrix.append(list(input()))
row_non_duplicates = [ [ "" for _ in range(m) ] for _ in range(n)]
vertical_non_duplicates = [ [ "" for _ in range(n) ] for _ in range(m)]

for i,row in enumerate(matrix):
    freq = Counter(row)
    for j,letter in enumerate(row):
        if freq[letter] == 1:
            row_non_duplicates[i][j] = letter

transposed_matrix = list(zip(*matrix))

for i,row in enumerate(transposed_matrix):
    freq = Counter(row)
    for j,letter in enumerate(row):
        if freq[letter] == 1:
            vertical_non_duplicates[i][j] = letter
col_non_duplicates = list(zip(*vertical_non_duplicates))

ans=[]
for i in range(n):
    for letter1, letter2 in zip(row_non_duplicates[i],col_non_duplicates[i]):
        if letter1 == letter2:
            ans.append(letter1)

print("".join(ans))