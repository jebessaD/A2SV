import math
def domino(numbers):
    num = numbers.split(" ")
    n= int(num[0])
    m=int(num[1])
    a=int(num[2])
    return (math.ceil(n/a) * math.ceil(m/a))
numbers=input("")
print(domino(numbers))