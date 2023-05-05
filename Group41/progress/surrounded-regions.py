class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        # """
        directions = [(0,1),(0,-1),(-1,0),(1,0)]
        def inbound(i,j):
            return 0 <= i < len(board) and 0 <= j < len(board[0])

        visited = set()

        def dfs(i,j):
            visited.add((i,j))
            board[i][j] = "Y"
            for r,c in directions:
                new_i = i + r
                new_j = j + c
                if inbound(new_i,new_j) and (new_i,new_j) not in visited and board[new_i][new_j] == "O":
                    
                    dfs(new_i,new_j)

        def onBorder(board):
            for i in [0,len(board)-1]:
                for j in range(len(board[i])):
                    if (i,j) not in visited and board[i][j]=="O":
                        dfs(i,j)

            
            for j in [0,len(board[0])-1]:
                for i in range(len(board)):
                    if (i,j) not in visited and board[i][j]=="O":
                        dfs(i,j)
 
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == "O":
                        board[i][j] = "X"
                    elif board[i][j] == "Y":
                        board[i][j] = "O"
        
        onBorder(board)
        