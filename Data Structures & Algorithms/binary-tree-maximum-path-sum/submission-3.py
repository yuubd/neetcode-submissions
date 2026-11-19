# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ''' 
        In the second example, if 10 node is indeed 50.
        Then is the output 70? Or still 40? I guess I am asking if I am maximizing the output

        either there are three options
        leftPathSum, rightPathSum, rightPathSum+leftPathSum

        base: 
        1. no node: return 0
        2. single node = return max(0, 0, -15) => 0
        3. trivial 3 nodes: return max(leftsum, rightsum, leftsum+rightsum+nodeval)
        '''
        self.maxSum = -math.inf
        def dfs(node):
            if node == None: 
                return 0
            leftSum, rightSum = max(0, dfs(node.left)), max(0, dfs(node.right))
            self.maxSum = max(self.maxSum, leftSum + rightSum + node.val)
            return max(leftSum, rightSum) + node.val
        
        dfs(root)
        return self.maxSum