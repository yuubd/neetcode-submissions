# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_indices = { val :idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0

        def dfs(l, r):
            if l > r:
                return None
            curr_val = preorder[self.pre_idx]
            curr_root = TreeNode(curr_val)
            self.pre_idx += 1
            curr_root_inorder_idx = inorder_indices[curr_val]

            curr_root.left = dfs(l, curr_root_inorder_idx-1)
            curr_root.right = dfs(curr_root_inorder_idx+1, r)
            
            
            return curr_root
        
        return dfs(0, len(preorder)-1)