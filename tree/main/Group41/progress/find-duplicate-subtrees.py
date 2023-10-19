# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        ans = []
        store = defaultdict(int)
        def dfs(root):

            if not root:
                return ""

            left_node = dfs(root.left)
            right_node = dfs(root.right)

            path = str(root.val) + "-" + left_node + "-" + right_node
            
            if store[path]==1:
                ans.append(root)

            store[path] += 1

            return path

        dfs(root)
        return ans

        