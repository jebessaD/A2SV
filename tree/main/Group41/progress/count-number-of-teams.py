class Solution:
    def numTeams(self, rating: List[int]) -> int:
#         
        n = len(rating)
        greater = [0] * n
        smaller = [0] * n
        count = 0
        
        for i in range(n):
            for j in range(i):
                if rating[j] < rating[i]:
                    count += greater[j]
                    greater[i] += 1
                else:
                    count += smaller[j]
                    smaller[i] += 1
        return count
                    