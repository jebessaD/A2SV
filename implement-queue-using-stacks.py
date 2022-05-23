class MyQueue:

    def __init__(self):
        self.MyQueue=[]

    def push(self, x: int) -> None:
        self.MyQueue.append(x)
        

    def pop(self) -> int:
        return self.MyQueue.pop(0)
        

    def peek(self) -> int:
        return self.MyQueue[0]

    def empty(self) -> bool:
        if(self.MyQueue):
            return False
        return True
 
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()