#solve using BFS/ Level order using queue
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
      if q is None and p is None:
        return True
      if q is None or p is None or p.val != q.val:
        return False
      
      left = self.isSameTree(p.left, q.left)
      right = self.isSameTree(p.right, q.right)
      # return True if left and right else False (# if left and right are true return True)
      return left and right
