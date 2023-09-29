class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()        

    def addWord(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_word = True
        

    def search(self, word: str) -> bool:
        stack = [(self.root,0)]

        while stack:
            curr , index = stack.pop()
            if index == len(word):
                if curr.is_word:
                    return True

            elif word[index] == ".":
                for child in curr.children.values():
                    stack.append((child,index+1))

            elif word[index] in curr.children:
                stack.append((curr.children[word[index]],index + 1))

        return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)