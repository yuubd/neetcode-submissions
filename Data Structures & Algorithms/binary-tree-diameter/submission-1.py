# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        when reaching the leaf node, compute the len of the nodes arr-1 and save the max
        the diameter is the sum of the heights of left and right sub trees

        for a node, get sum of children_node (recursion)
            base case, if node is null, return 0
            recursion step: 
                computute the diameter by summing two results
                retuen the max of two + 1
        Compute the max diameter
        return the diameter
        '''
        
        if not root: return 0

        self.max_d = 0
        def diameterOfBinaryTreeHelper(node, d) -> int:
            if not node: return 0
            left_h = diameterOfBinaryTreeHelper(node.left, d)
            right_h = diameterOfBinaryTreeHelper(node.right, d)
            self.max_d = max(self.max_d, left_h + right_h)

            return max(left_h, right_h) + 1
        
        diameterOfBinaryTreeHelper(root, self.max_d)
        return self.max_d
        
        

        