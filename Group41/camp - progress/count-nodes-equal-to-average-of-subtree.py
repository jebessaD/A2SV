# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        self.nodes = 0
        self.count = 0
        def calculateAverage(root):
            if not root:
                return 0,0
            left_sum, left_node = calculateAverage(root.left)
            right_sum, right_node = calculateAverage(root.right)
            
            self.sum = left_sum + right_sum + root.val
            self.nodes = right_node + left_node + 1

            if self.sum // self.nodes == root.val:
                self.count += 1

            return self.sum , self.nodes

        calculateAverage(root)
        return self.count