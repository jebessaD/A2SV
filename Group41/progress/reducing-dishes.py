class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        sum_ = 0
        satisfaction.sort()
        flag = 0
        for i in range(len(satisfaction)-1,-1,-1):
            sum_ += satisfaction[i]
            if sum_ < 0:
                flag = 1
                break

        start = i + flag
        ans = 0

        for curr in range(start,len(satisfaction)):
            ans += (curr - start + 1) * satisfaction[curr]
        return ans


                