# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.sum_ = 0
        store = Counter([0])
        self.count = 0
        def backtrack(root):
            if not root:
                return
            
            self.sum_ += root.val

            if self.sum_ - targetSum in store:
                self.count += store[self.sum_ - targetSum]

            store[self.sum_] = store.get(self.sum_, 0) + 1

            backtrack(root.left)
            backtrack(root.right)

            store[self.sum_] -= 1
            if store[self.sum_] == 0:
                store.pop(self.sum_)

            self.sum_ -= root.val

        backtrack(root)
        return self.count