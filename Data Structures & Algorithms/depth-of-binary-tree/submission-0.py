# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        base if None => return the depth
        a node returne max(left+1, right+1)
        '''
        return self.maxDepthHelper(root, 0)

    def maxDepthHelper(self, node, depth) -> int:
        if node == None: return depth
        return max(self.maxDepthHelper(node.left, depth+1), self.maxDepthHelper(node.right, depth+1))

        