import sys
sys.setrecursionlimit(200000)
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        '''
        11:13 -> 57
        Guarentee BS meaning all are unique?
        Can it be from a val to same val?
        are we also guarenteed to have start and dest val in the tree?

        1. need to find the path to from and to using dfs backtracking
        2. the path is all U from to the common parent

        state
            fromPath
            toPath
            def dfs(n, dest, path):
                if dest is n, return True the path
                append the n.val
                recurse to left first and right
            
            find the common parent
            from the root, scan the two path until they split,
            pathA [1 2 4] pathB [(1, root) (3, R) (7, R)] the idx = 0
            U * len(pathA[idx+1:]) + extract the path pathB[ids+1:]

            0 start
              1 dest R 
        '''

        def dfs(n, target, path):
            # print(path)
            if n == None:
                return []

            if target == n.val:
                return path.copy()

            path.append("L")
            leftPath = dfs(n.left, target, path) 
            if leftPath:
                return leftPath
            path.pop()

            path.append("R")
            rightPath = dfs(n.right, target, path)
            if rightPath:
                return rightPath
            path.pop()
            return []
        
        pathA = dfs(root, startValue, ['ROOT']) # start
        # print('pathA', pathA)
        pathB = dfs(root, destValue, ['ROOT']) # dest
        # print('pathB', pathB)

        i = 0 # last common parent after while
        while True:
            if i >= len(pathA) or i >= len(pathB) or pathA[i] != pathB[i]:
                break
            i += 1
        # print(i)
        # print("pathA[i:]", pathA[i:])
        # print("pathB[i+1:]", pathB[i:])
        return "U"*len(pathA[i:]) + ''.join([path for path in pathB[i:]]) # might check the idx err
        
            


















