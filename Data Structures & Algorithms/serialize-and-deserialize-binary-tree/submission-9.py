# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        '''
            1. For DFS, we need to identify base cases.
            2. when node is None, append 'N' 
            3. append node.val to the global data var
            4. dfs on left node and then right node.
            delimiter join the list
            This will build the data in preorder
        '''
        if not root: return ''

        data = []
        def dfs(node):
            if node == None:
                data.append('N')
                return
            data.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return '#'.join(data)

            
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        '''
            For desirialize,
            1. split the data with the delimiter
            2. create a root node pass to def dfs(node)
            3. dfs will do:
                1) if 'N': return None
                2) else create a node with the value at i which is also a global var
                3) call dfs on left node and then right node. 
            This way the i will increment one by one with the preorder order
        '''
        if data == '': return None

        nodeList = data.split('#')
        print(nodeList)
        i = 0
        def dfs():
            nonlocal i
            if i > len(nodeList):
                return None
            val = nodeList[i]
            i += 1
            if val == "N":
                return None
            node = TreeNode(int(val))
            
            node.left = dfs()
            node.right = dfs()

            return node
            
        return dfs()







    def serializeBFS(self, root: Optional[TreeNode]) -> str:
        if not root: return ''

        data = []
        q = deque([root])
        while q:
            node = q.popleft()
            if not node:
                data.append('N')
                continue
            data.append(str(node.val))
            q.append(node.left)
            q.append(node.right)
        return '#'.join(data)

            
        
    # Decodes your encoded data to tree.
    def deserializeBFS(self, data: str) -> Optional[TreeNode]:
        if data == '': return None

        nodes = data.split('#')
        res = TreeNode(nodes[0])
        q = deque([res])
        i = 1
        while q:
            node = q.popleft()

            if nodes[i] != 'N':
                node.left = TreeNode(nodes[i])
                q.append(node.left)
            i += 1
            if nodes[i] != 'N':
                node.right = TreeNode(nodes[i])
                q.append(node.right)
            i += 1

        return res



