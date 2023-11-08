# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(root,n):
            
            if not root:
                return 0

            dfs(root.left,n*2)
            if not root.left and not root.right and not n%2:
                self.ans += root.val
            dfs(root.right,2*n+1)

        dfs(root,1)
        return self.ans

        