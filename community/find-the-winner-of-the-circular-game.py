class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players=[i+1 for i in range(n)]
        def winner (array):
            if(len(array)==1):
                return array[0]
            elif(len(array)<k):
                rem=k%len(array)
                if(rem==0):
                    rem=len(array)
                return winner(array[rem:len(array)]+array[0:rem-1])
            
            else:
                return winner(array[k:len(array)]+array[0:k-1]) 
        return winner(players)