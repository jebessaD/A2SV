# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        if len(preorder) == 0:
            return None

        pos = bisect.bisect(preorder[1:],preorder[0])
        root = TreeNode(preorder[0])
        root.left = self.bstFromPreorder(preorder[1:pos+1])
        root.right = self.bstFromPreorder(preorder[pos+1:])
        return root

        