# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        graph = defaultdict(list)
        queue = deque()
        queue.append(root)

        while queue:
            parent = queue.popleft()

            if parent.left:
                graph[parent.left.val].append(parent.val)
                graph[parent.val].append(parent.left.val)
                queue.append(parent.left)

            if parent.right:
                graph[parent.right.val].append(parent.val)
                graph[parent.val].append(parent.right.val)
                queue.append(parent.right)

      
        queue.append((target.val,0))
        visited = set()
        visited.add(target.val)
        ans = []
        while queue:
            parent,length = queue.popleft()
            if length == k:
                ans.append(parent)

            for child in graph[parent]:
                if child not in visited:
                    queue.append((child,length + 1))
                    visited.add(child)
                

        return ans

