class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        store_diagonal=defaultdict(set)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                store_diagonal[i-j].add(matrix[i][j])
                if len(store_diagonal[i-j]) > 1:
                    return False
        return True