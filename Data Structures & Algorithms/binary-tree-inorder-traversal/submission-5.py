# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # bfs

        # bfs
        res = []
        st = []
        curr = root
        while curr or st:
            while curr != None: # if left is there, go to left first before appending the curr
                st.append(curr)
                curr = curr.left
            curr = st.pop()
            res.append(curr.val)
            curr = curr.right
        return res

        
        res = []
        st = []
        curr = root
        while curr or st:
            if curr != None: # if left is there, go to left first before appending the curr
                st.append(curr)
                curr = curr.left
            else: # there is no more left, append the curr val and go to the right
                curr = st.pop() 
                res.append(curr.val)
                curr = curr.right
        return res


        # dfs
        res = []

        def dfs(node):
            if node == None:
                return
            
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
            
        dfs(root)
        return res