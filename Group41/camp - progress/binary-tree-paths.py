# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        curr = [str(root.val)]
        def findLeaf(root,curr,ans):
            if not root.left and not root.right:
                ans.append("->".join(map(str,curr)))
                return 

            if root.left :
                curr.append(root.left.val)
                findLeaf(root.left,curr,ans)
                curr.pop()

            if root.right:
                curr.append(root.right.val)
                findLeaf(root.right,curr,ans)
                curr.pop()

        findLeaf(root,curr,ans)
        return ans



        