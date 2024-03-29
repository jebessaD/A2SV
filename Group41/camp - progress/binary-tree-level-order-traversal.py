# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_store = defaultdict(list)
        def findLevel(root, level):
            if not root:
                return

            level_store[level].append(root.val)

            findLevel(root.left, level + 1)
            findLevel(root.right, level + 1)
        findLevel(root,0)
        return level_store.values()

            

