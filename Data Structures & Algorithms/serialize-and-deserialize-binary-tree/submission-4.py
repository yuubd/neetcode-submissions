# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root: return ''

        data = []
        q = deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if not node:
                    data.append('N')
                    continue
                data.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        return '#'.join(data)

            
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == '': return None
        
        nodes = data.split('#')
        print(nodes)
        lv = 1
        res = TreeNode(nodes[0])
        q = deque([res])
        i = 1
        while q:
            node = q.popleft()
            if node == None:
                continue

            if nodes[i] != 'N':
                node.left = TreeNode(nodes[i])
                
                q.append(node.left)
            i += 1
            if nodes[i] != 'N':
                node.right = TreeNode(nodes[i])
                
                q.append(node.right)
            i += 1


        return res





