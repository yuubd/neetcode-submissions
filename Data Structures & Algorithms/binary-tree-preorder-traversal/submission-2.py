# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        st = [root]
        curr = None

        while st:
            cur = st.pop()
            if cur == None: 
                continue
            
            res.append(cur.val)
            st.append(cur.right)
            st.append(cur.left)
        
        return res

        
        
        
        
        
        res = []
        
        def dfs(node):
            if node == None:
                return
            
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return res