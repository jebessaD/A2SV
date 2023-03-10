# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#space O(1)
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.prev = None
        self.count = 1
        self.max_count = 1
        self.ans = []
        def inorderTraversal(node):
            if not node:
                return 
            inorderTraversal(node.left)

            if self.prev == node.val:
                self.count += 1
            else:
                self.count = 1

            self.prev = node.val

            if self.count > self.max_count:
                self.max_count = self.count
                self.ans = [node.val]
            elif self.count == self.max_count:
                self.ans.append(node.val)

            inorderTraversal(node.right)

        inorderTraversal(root)
        return self.ans
    
#space O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        store = Counter()
        def countNode(root,store):
            if not root:
                return 
            store[root.val] += 1
            countNode(root.left,store)
            countNode(root.right,store)

        countNode(root,store)
        store = dict(sorted(store.items(), key=lambda x: x[1], reverse=True))
        ans = []
        print(store)
        for key in store:
            if not ans:
                ans.append(key)
            elif store[ans[-1]] == store[key]:
                ans.append(key)
            else:
                break
            
        return ans

    

