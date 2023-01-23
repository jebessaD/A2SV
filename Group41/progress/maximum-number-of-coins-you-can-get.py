
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        ans=0
        piles.sort()
        me=len(piles)-2
        bob=0
        while bob < me:
            ans += piles[me]
            me -= 2
            bob+=1

        return ans


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        print(piles)
        sum=0
        for i in range(len(piles)//3):
            sum+=piles[2*i+1]
        return sum
            
        