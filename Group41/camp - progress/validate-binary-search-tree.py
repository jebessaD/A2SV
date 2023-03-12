# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = float("-inf")
        self.valid = True
        
        def checkValidity(root):
            if not root:
                return 
            
            checkValidity(root.left)

            if self.prev >= root.val:
                self.valid = False
                return 
            self.prev = root.val

            checkValidity(root.right)
        checkValidity(root)
        return self.valid