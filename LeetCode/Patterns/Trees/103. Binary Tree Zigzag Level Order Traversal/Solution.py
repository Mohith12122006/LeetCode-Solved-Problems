from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        res = []
        turn = 0
        while queue:
            level = []
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)

                if node.right is not None:
                    queue.append(node.right)
                if node.left is not None:
                    queue.append(node.left)
                
            if turn%2 != 0:
                res.append(level)
            else: res.append(level[::-1])
            turn += 1
        return res
        