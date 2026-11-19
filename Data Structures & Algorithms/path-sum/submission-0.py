# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(n, currSum):
            if n == None:
                return False
            if currSum+n.val == targetSum and n.left == None and n.right == None:
                return True
            if dfs(n.left, currSum+n.val) or dfs(n.right, currSum+n.val):
                return True
            return False
        
        return dfs(root, 0)
