# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.graph = []
        self.index = 0
        for k in nestedList:
            self.dfs(k)
    
    def dfs(self,node):
        if not node:
            return
            
        if node.isInteger():
            self.graph.append(node)
        else:
            li = node.getList()
            for i in li:
                self.dfs(i)
        
              
    def next(self) -> int:
        self.index += 1
        return self.graph[self.index - 1]
    
        
        
    def hasNext(self) -> bool:
        return self.index < len(self.graph)
         

# Your NestedIterator object will be instantiated and called as such:
# i, node = NestedIterator(nestedList), []
# while i.hasNext(): node.append(i.next())