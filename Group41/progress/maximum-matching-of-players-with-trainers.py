class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        ptr1=0
        ptr2=0
        ans=0
        players.sort()
        trainers.sort()
        while ptr1 < len(players) and ptr2 < len(trainers):
            if players[ptr1] <= trainers[ptr2]:
                ptr1 += 1
                ptr2 += 1
                ans += 1
            else:
                ptr2 += 1

        return ans