class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        valid=[]
        for i,j in points:
            if i==x or j==y:
                valid.append([i,j])

        if not valid:return -1
        minimum=abs(x-valid[0][0])+ abs(y-valid[0][1])
        ans=valid[0]
        for m,n in valid:
            if abs(x-m) + abs(y-n) < minimum:
                minimum=abs(x-m) + abs(y-n)
                ans=[m,n]

        return points.index(ans)


