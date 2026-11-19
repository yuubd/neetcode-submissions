# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        TRAVERSE AND IF ANYTHING IS NOT EQUAL, RETURN FALSE.
        base cases:
        1. (nil, nil)
           if both are nil, return true

        2. (1, 1)
           if values are same, return isSameTree(left nodes of both) and isSameTree(right nodes of both)
        3. (1, 2) or (1 nil) or (nil 1)
           if vals are different, return false
        '''

        if p == None and q == None: 
            return True

        # We dont allow None below
        if p == None or q == None or p.val != q.val:
            return False
        
        # vals are same
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)








        