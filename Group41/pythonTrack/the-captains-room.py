from collections import Counter
k = input()
rooms= Counter(input().split(" ")).most_common()
print(rooms[-1][0])