# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None: return []
        
        res = []
        q = deque([root])
        
        while len(q) > 0:
            curr_lv = []
            for _ in range(len(q)): # the len will increase for the # of children
                curr_n = q.popleft()

                # add to curr lv values
                curr_lv.append(curr_n.val)
                
                # add children
                if curr_n.left != None:
                    q.append(curr_n.left)
                if curr_n.right != None:
                    q.append(curr_n.right)
            
            res.append(curr_lv)
        
        return res
        