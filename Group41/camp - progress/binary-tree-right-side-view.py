# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        store = {}
        def findRight(root,level):
            if not root:
                return 
            
            store[level] = root.val
            findRight(root.left,level + 1)
            findRight(root.right,level + 1)
            
        findRight(root,0)
        return store.values()