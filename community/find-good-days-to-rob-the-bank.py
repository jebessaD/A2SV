class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        def countDecrease(array):
            prefix=[0]
            for i in range(len(array)-1):
                if array[i]>=array[i+1]:
                    prefix.append(prefix[i]+1)
                else:
                    prefix.append(0)
            return prefix
        forward=countDecrease(security)
        security.reverse()
        backward=countDecrease(security)
        backward.reverse()
        ans=[]
        for i,(x,y) in enumerate(zip(forward,backward)):
            if x >=time and y>=time:
                ans.append(i)
        return ans
