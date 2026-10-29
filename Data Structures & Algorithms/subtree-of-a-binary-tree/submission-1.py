# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True 
        if not root: return False
        if self.sameTree(root,subRoot):
            return True 
        if self.isSubtree(root.left,subRoot) or self.isSubtree(root.right, subRoot):
            return True 
        else: return False


    def sameTree(self, s,r):
        if not s and not r:
            return True 
        if s and r and s.val == r.val:
            return self.sameTree(s.left, r.left) and self.sameTree(s.right, r.right)
        return False


        