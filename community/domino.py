def domino(numbers):
    num = numbers.split(" ")
    area= int(num[0])*int(num[1])
    return area//2
numbers=input("")
print(domino(numbers))