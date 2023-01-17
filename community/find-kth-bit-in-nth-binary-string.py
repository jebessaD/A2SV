class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def reverseBit(arr):
            return arr.replace("0","-").replace("1","0").replace("-","1")
        
        def finder(n):
            if(n==1):
                return "0"
            return (finder(n-1) + "1" + reverseBit(finder(n-1))[::-1])
        
        return finder(n)[k-1]
        