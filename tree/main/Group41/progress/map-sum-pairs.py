class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
        

class MapSum:

    def __init__(self):    
        self.root = TrieNode()
        self.visited = {}

    def insert(self, key: str, val: int) -> None:
        curr = self.root
        curr_val = val
        if key in self.visited:
            curr_val = val - self.visited[key]
        
        self.visited[key] = val

        for char in key:
            if char not in curr.children:
                curr.children[char] = TrieNode()

            curr = curr.children[char]
            curr.count += curr_val

    def sum(self, prefix: str) -> int:
        curr = self.root
        ans = 0

        for char in prefix:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]

        return curr.count
            

        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)