class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        directions=[[-1,0],[1,0],[0,1],[0,-1],[1,-1],[1,1],[-1,1],[-1,-1]]

        def travel(direction, queens):
            moved_king=king.copy()
            while max(moved_king) < 8 and min(moved_king)>=0:
                moved_king[0] += direction[0]
                moved_king[1] += direction[1]
                if moved_king in queens:
                    return moved_king
        ans=[]
        for direction in directions:
            res=travel(direction,queens)
            if res:
                ans.append(res)

        return ans