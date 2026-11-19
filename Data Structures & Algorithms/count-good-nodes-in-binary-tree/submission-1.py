# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root == None: return 0

        self.res = 0
        def dfs(node, maxSoFar):
            if node == None: return

            if node.val >= maxSoFar: 
                self.res += 1

            dfs(node.left, max(maxSoFar, node.val))
            dfs(node.right, max(maxSoFar, node.val))

        dfs(root, root.val)
        return self.res











