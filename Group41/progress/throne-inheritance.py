class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.graph = defaultdict(list)
        self.dead = set()
        

    def birth(self, parentName: str, childName: str) -> None:
        self.graph[parentName].append(childName)
        

    def death(self, name: str) -> None:
        self.dead.add(name)
        

    def getInheritanceOrder(self) -> List[str]:
        visited = set()
        order = []

        def dfs(parent):
            if parent not in self.dead:
                order.append(parent)
            visited.add(parent)

            for child in self.graph[parent]:
                if child not in visited:
                    dfs(child) 

        dfs(self.kingName)
        return order
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()g