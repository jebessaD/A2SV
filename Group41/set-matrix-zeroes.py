class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_index = [set(),set()]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    zero_index[0].add(row)
                    zero_index[1].add(col)
        
        for new_row in range(len(matrix)):
            for new_col in range(len(matrix[0])):
                if new_row in zero_index[0] or new_col in zero_index[1]:
                    matrix[new_row][new_col] = 0