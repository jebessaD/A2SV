class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        def rotateCounter(matrix):
            rotatedClockwise = list(zip(*matrix))
            return list(reversed(rotatedClockwise))

        ans = []
        while len(matrix) > 0:
            poped = matrix.pop(0)
            ans.extend(poped)
            matrix = rotateCounter(matrix)

        return ans