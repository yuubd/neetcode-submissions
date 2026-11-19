# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        1. Construct a map of val: idx for inorder tree
        2. start from preorder with i (initially 0) the root, get the idx in inorder. 
            The size of left tree is idx(any root but the real root initially) - l(initially 0)
            The size of right tree is r(the right end. len(inorder)-1 initially) - idx + 1
        3. set the value of root node, dfs to left with i+1 and dfs to right with i + size of left tree (no need +1 as it s index based).
        4. if the size of any sub tree is 0, assign null.
        '''

        inorderMap = { n:i for i, n in enumerate(inorder) }

        def dfs(l, r, i): # l r is the range of the current tree and i is the idx of the root value in preorder 
            if l > r:
                return None
                # 0, 0, 1(preorder == 2)
            root = preorder[i]
            rootIdx = inorderMap[root]
            leftSize = rootIdx - l

            node = TreeNode(root)
            node.left = dfs(l, rootIdx-1, i+1)
            node.right = dfs(rootIdx+1, r, i+1+leftSize)

            return node
        return dfs(0, len(inorder)-1, 0)














    def buildTree2(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
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