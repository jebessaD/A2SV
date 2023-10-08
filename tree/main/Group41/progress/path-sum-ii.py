# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.ans = []
        def trackPath(root,sum_,path,ans):
            if not root:
                return 

            if sum_ == targetSum and not(root.left or root.right):
                self.ans.append(path.copy())

            if root.left:
                path.append(root.left.val)
                trackPath(root.left,sum_ + root.left.val,path,ans)
            
            if root.right:
                path.append(root.right.val)
                trackPath(root.right,sum_ + root.right.val,path,ans)
            leaf = path.pop()
            sum_ -= leaf

        if not root:
            return []
        
        trackPath(root,root.val,[root.val],[])
        return self.ans


