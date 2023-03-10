# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        root1= root.left
        root2 = root.right

        def checkSymmetric(root1,root2):
            if not root2 and not root1:
                return True

            if (not root2 and root1) or (not root1 and root2):
                return False

            if root1.val != root2.val:
                return False

            return checkSymmetric(root1.left,root2.right) and checkSymmetric(root1.right,root2.left)
        return checkSymmetric(root1,root2)