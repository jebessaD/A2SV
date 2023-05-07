# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        queue = deque()
        queue.append(root)
        ans = []
        while queue:
            sum_ = 0
            count = 0
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                sum_ += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            ans.append(sum_/length)

        return ans
    


            