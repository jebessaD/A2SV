class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sub_board = [list(zip(*board[:3])),list(zip(*board[3:6])),list(zip(*board[6:9]))]
        for three_rows in sub_board:
            output = set()
            count = 0
            
            for inx ,row in enumerate(three_rows):
                for num in row:
                    if num.isnumeric():
                        count += 1
                        output.add(num)

                if len(output) != count:
                    return False

                if (inx + 1) % 3 == 0:
                    output = set()
                    count=0
                    
        def checkRowDuplicate(board):
            for eachrow in board:
                len_dot = eachrow.count(".")
                len_num = len(set(eachrow))

                if len_dot:
                    len_num -= 1

                if len_num != 9 - len_dot:
                    return True

        ans1 = checkRowDuplicate(board)
        ans2 = checkRowDuplicate(list(zip(*board)))
        if ans1 or ans2:
            return False

        return True
            


                
