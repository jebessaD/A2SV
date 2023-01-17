class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        print(piles)
        sum=0
        for i in range(len(piles)//3):
            sum+=piles[2*i+1]
        return sum