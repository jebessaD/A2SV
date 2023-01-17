class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players=[i+1 for i in range(n)]
        curr=0
        while len(players)>1:
            curr = curr+ k-1
            curr%=len(players)
            players.pop(curr)

        return players.pop()