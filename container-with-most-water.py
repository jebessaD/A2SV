class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1=0
        p2=len(height)-1
        maximum=0
        
        while(p2>p1):
            if(height[p1]<height[p2]):
                area= height[p1] * (p2-p1)
                p1+=1
            else:
                area= height[p2] * (p2-p1)
                p2-=1
            if(area>maximum):
                maximum=area
        return maximum