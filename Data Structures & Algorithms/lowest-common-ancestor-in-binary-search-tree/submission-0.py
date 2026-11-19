# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        small, large = (p.val, q.val) if p.val <= q.val else (q.val, p.val)
        while not (small <= root.val and root.val <= large):
            root = root.left if large < root.val else root.right
        return root