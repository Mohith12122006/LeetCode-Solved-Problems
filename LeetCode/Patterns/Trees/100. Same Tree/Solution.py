# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and q: return False

        stack = [(p,q)]
        while stack:

            curr1, curr2 = stack.pop()

            if curr1 == None and curr2 == None:
                continue
            
            if curr1 is None or curr2 is None:
                return False
            
            if curr1.val != curr2.val: return False

            stack.append((curr1.left,curr2.left))
            stack.append((curr1.right,curr2.right))
        
        return True
        