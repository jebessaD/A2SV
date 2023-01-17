class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        reshaped=[]
        temp=[]
        if r * c != len(mat)* len(mat[0]):
            return mat

        for row in mat:
            for col in row:
                temp.append(col)
                if len(temp) == c:
                    reshaped.append(temp)
                    temp=[]

        return reshaped