# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        st = []
        curr = root
        while len(st) > 0 or curr is not None:

            while curr is not None:
                st.append(curr)
                curr = curr.left
            
            # found the lowest, the st's last elem is the smallest
            # curr = None at this moment
            curr = st.pop()
            k -= 1

            if k == 0:
                return curr.val
            
            # before checking one level upper, 
            # check the curr node's right nodes 
            # which are less then the upper level node 
            curr = curr.right
        return 0
        
    def kthSmallestSortedArr(self, root: Optional[TreeNode], k: int) -> int:

        sorted_vals = []
        def inorder(node):
            if node is None: return

            inorder(node.left)
            sorted_vals.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return sorted_vals[k-1]