# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
        1. find the root of sub in the main
        2. run same tree
        '''

        def same_trees(n1, n2):
            if n1 == None and n2 == None: return True
            if n1 == None or n2 == None or n1.val != n2.val: return False
            return same_trees(n1.left, n2.left) and same_trees(n1.right, n2.right)


        if subRoot == None: return True
        if root == None: return False

        q = deque()
        q.append(root)

        while len(q) > 0:
            curr_n = q.popleft()
            if curr_n == None:
                continue
            # found starting point.  
            # if the val are unique, we can return, if not, is_subtree = ...
            if curr_n.val == subRoot.val:
                if same_trees(curr_n, subRoot): 
                    return True

            q.append(curr_n.left)
            q.append(curr_n.right)
        
        return False



        