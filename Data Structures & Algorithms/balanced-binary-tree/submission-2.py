# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
        every node should be balanced
        base case: if None, return 0
        recursion step: get height of l and r => compare l r, if balanced => return max of l r + 1
        return 
        '''

        self.balanced = True
        def isBalancedHelper(node) -> int:
            if node == None: return 0
            
            l_height = isBalancedHelper(node.left)
            r_height = isBalancedHelper(node.right)
            
            if l_height == -1 or l_height == -1: return -1

            if abs(l_height - r_height) > 1:
                self.balanced = False
                return -1
            
            return 1 + max(l_height, r_height)
        
        

        isBalancedHelper(root)
        return self.balanced








