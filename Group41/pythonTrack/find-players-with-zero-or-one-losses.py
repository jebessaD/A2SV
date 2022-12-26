class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner={}
        loser={}
        players=set()
        for x,y in matches:
            players.add(x)
            players.add(y)
            if y in loser:
                loser[y]+=1
            else:
                loser[y]=1
        ans=[[],[]]
        for p in loser:
            if loser[p]==1:
                ans[1].append(p)
        for n in players:
            if n not in loser:
                ans[0].append(n)      
        return [sorted(ans[0]),sorted(ans[1])]