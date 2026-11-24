# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        '''
        need to store in order array
        next will return the 
        '''
        self.idx = 0
        self.inOrder = []

        st = []
        cur = root
        while cur or st:
            while cur:
                st.append(cur)
                cur = cur.left
            cur = st.pop()
            self.inOrder.append(cur.val)
            cur = cur.right
        print(self.inOrder)






        def dfs(node):
            if node == None:
                return
            
            dfs(node.left)
            self.inOrder.append(node.val)
            dfs(node.right)
        # dfs(root)

    def next(self) -> int:
        if self.idx < len(self.inOrder):
            self.idx += 1
        return self.inOrder[self.idx-1]

    def hasNext(self) -> bool:
        return self.idx < len(self.inOrder)




# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()