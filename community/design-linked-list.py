class MyLinkedList:

    def __init__(self):
        # self.val = x
        self.llist=[]
        
    def get(self, index: int) -> int:
        if(index<len(self.llist) and index>=0):
            return (self.llist[index])
        return -1
    
    def addAtHead(self, val: int) -> None:
        self.llist.insert(0,val)

        

    def addAtTail(self, val: int) -> None:
        self.llist.append(val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        if(len(self.llist)>=index):
            self.llist.insert(index,val)
        
        

    def deleteAtIndex(self, index: int) -> None:
        if(len(self.llist)>index):
            self.llist.pop(index)
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)