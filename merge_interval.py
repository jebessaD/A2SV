class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[1])
        intervals.sort(key = lambda x: x[0])
        a1=intervals[0][0]
        b1=intervals[0][1]

        newList=[]
        tempList=[a1,b1]
        print(intervals)

        counter=0
        for arr in intervals:
            a2=arr[0]
            b2=arr[1]
            if (b1>=a2 and b1 <= b2):
                b1=b2
                tempList[0]=a1
                tempList[1]=b1
            elif(b1>=a2 and b1 > b2):
                print("section b")
            else:
                t=tempList.copy()
                newList.append(t)
                a1=a2
                b1=b2
                tempList[0]=a1
                tempList[1]=b1
        newList.append(tempList)

        return(newList)