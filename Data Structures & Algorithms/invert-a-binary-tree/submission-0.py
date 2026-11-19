# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        base
        []: if node/root is null then return
        [3 2 1]: save self node to tmp, switch with the right and then return the root.

        base case: return at null
        invertTree on the children
        switch children
        '''

        if root == None:
            return root
        
        self.invertTree(root.left)
        self.invertTree(root.right)

        tmp = root.left
        root.left = root.right
        root.right = tmp

        return root