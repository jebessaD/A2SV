class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        myList=[]
        for num in range(1,n+1):
            if num%3 == 0 and num%5== 0:
                myList.append("FizzBuzz")
            elif num%3==0:
                myList.append("Fizz")
            elif num%5==0:
                myList.append("Buzz")
            else:
                myList.append(str(num))
        return myList
                
            