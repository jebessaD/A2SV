class MyCircularDeque:

    def __init__(self, k: int):
        self.MyQueue=[]
        self.k=k
        

    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            
            self.MyQueue.insert(0,value)
            return True
        return False

    def insertLast(self, value: int) -> bool:
         if (not self.isFull()):
            self.MyQueue.append(value)
            return True
         return False
        
    def deleteFront(self) -> bool:
        if not self.isEmpty():
            self.MyQueue.pop(0)
            return True
        return False
        

    def deleteLast(self) -> bool:
        if not self.isEmpty():
            self.MyQueue.pop()
            return True
        return False
        

    def getFront(self) -> int:
        if not self.isEmpty():
            return self.MyQueue[0]
        return -1
        

    def getRear(self) -> int:
        if not self.isEmpty():
            return self.MyQueue[-1]
        return -1
        

    def isEmpty(self) -> bool:
        if len(self.MyQueue)==0:
            return True
        return False
            
        

    def isFull(self) -> bool:
        if len(self.MyQueue)==self.k:
            return True
        return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = self.MyQueue=[](k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()