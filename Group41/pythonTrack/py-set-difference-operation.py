# Enter your code here. Read input from STDIN. Print output to STDOUT
input()
english=set(input().split(" "))
input()
france=set(input().split(" "))
print(len(english.difference(france)))
