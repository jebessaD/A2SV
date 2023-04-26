# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        print(root)
        self.ans = 0
        def dfs(root,curr):
            curr = curr * 10 + root.val
            if not root.right and not root.left:
                self.ans += curr
                return
                
            if root.left:
                dfs(root.left,curr)
                
            if root.right:
                dfs(root.right,curr)
                
            curr //= 10 

        dfs(root,0)
        return self.ans