class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i,j,top,left,right,bottom=0,0,0,0,len(matrix[0]),len(matrix)
        output=[]
        while(left<right and top<bottom):
            while (j<right):
                output.append(matrix[i][j])
                j+=1
            top+=1
            i+=1
            j-=1
            while(i<bottom):
                output.append(matrix[i][j])
                i+=1
            right-=1
            j-=1
            i-=1
            while(j>=left):
                output.append(matrix[i][j])
                j-=1
            bottom-=1
            i-=1
            j+=1
            while(i>=top):
                output.append(matrix[i][j])
                i-=1
            left+=1
            i+=1
            j+=1
        return output[0:len(matrix)*len(matrix[0])]
            
        