# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def binaryTree(root, path = []):
            path.append(str(root.val))
            if not root.left and not root.right:
                ans.append("->".join(path))
                return
            
            if root.left:
                binaryTree(root.left, path)
                path.pop()
                
            if root.right:
                binaryTree(root.right, path)
                path.pop()
        binaryTree(root, [])
        return ans