# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        store = defaultdict(lambda: [float('inf'),0])
        max_width = defaultdict(int)
        
        def traverse(root,n,ind):

            if not root:
                return 

            
            traverse(root.left,n+1,2*ind)
            store[n][0] = min(store[n][0],ind)
            store[n][1] = max(store[n][1],ind)
            max_width[n] = store[n][1]  - store[n][0]
            traverse(root.right,n+1,2*ind+1)
        traverse(root,1,1)
        
        return max(max_width.values()) + 1


            
        