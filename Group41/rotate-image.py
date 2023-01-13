class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def transpose(matrix):
            for i in range(len(matrix)):
                for j in range(i+1,len(matrix)):
                    matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

            return matrix
        
        def swap(matrix):
            for row in matrix:
                left=0
                right=len(row)-1
                while left < right:
                    row[left],row[right] = row[right],row[left] 
                    right -= 1
                    left += 1

            return matrix

        transpose(matrix)
        swap(matrix)