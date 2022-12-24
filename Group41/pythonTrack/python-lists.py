if __name__ == '__main__':
    N = int(input())
    arr=[]
    for i in range(N):
        opp=input().split(" ")
        if opp[0]=="insert":
            arr.insert(int(opp[1]),int(opp[2]))
        elif opp[0]=="print":
            print(arr)
        elif opp[0]=="remove":
            arr.remove(int(opp[1]))
        elif opp[0]=="append":
            arr.append(int(opp[1]))
        elif opp[0]=="sort":
            arr.sort()
        elif opp[0]=="pop":
            arr.pop()
        elif opp[0]=="reverse":
            arr.reverse()