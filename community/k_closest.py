class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        myDict={}
        for index,point in enumerate(points):
            distance=point[0]**2 + point[1]**2
            myDict[(distance,index)]=point
        sorted_values=dict(sorted(myDict.items(), key=lambda item: item[0]))
        return(list(sorted_values.values())[:k])
