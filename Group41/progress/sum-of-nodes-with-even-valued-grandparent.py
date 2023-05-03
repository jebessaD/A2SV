# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        grand_parent = 1
        parent = root.val
        self.ans = 0

        def dfs(root,parent,grand_parent):
            if not root:
                return 
                
            if grand_parent % 2 == 0 and root.right:
                self.ans += root.right.val

            if grand_parent % 2 == 0 and root.left:
                self.ans += root.left.val

            if root.left:
                dfs(root.left,root.left.val,parent)
            if root.right:
                dfs(root.right,root.right.val,parent)

        dfs(root,parent,grand_parent)
        return self.ans
    

            