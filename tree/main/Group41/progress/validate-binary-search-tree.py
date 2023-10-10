# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = [float("-inf")]
        valid = [True]
        
        def checkValidity(root):
            if not root:
                return 
            
            checkValidity(root.left)

            if prev[0] >= root.val:
                valid[0] = False
                return 
                
            prev[0] = root.val

            checkValidity(root.right)
        checkValidity(root)
        return valid[0]