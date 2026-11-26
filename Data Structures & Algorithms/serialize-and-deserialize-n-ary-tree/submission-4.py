"""
# Definition for a Node.
class Node(object):
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        if children is None:
            children = []
        self.val = val
        self.children = children
"""

class Codec:

    '''
    cuz this n-ary, serialize
    #1@3 #3@2 #2@0 #4@0 #5@0 #6@0

    when deserialize,
    dfs with two loops and store next children(the sum of @Ns) and switch for next depth
    '''
    def serialize(self, root: 'Node') -> str:
        '''
        record the number of children use #val@len << next len nodes are the children

        #1@3 #3@2 #2@1 #4@0 #5@0 #6@0 #9@0
        '''

        if root == None:
            return ""

        res = []
        curlv = deque([root])
        while curlv: # there is any nodes in the q
            nextlv = deque()
            while curlv:
                curNode = curlv.popleft()
                res.append("#" + str(curNode.val) + "@" + str(len(curNode.children)))
                
                for child in curNode.children:
                    nextlv.append(child)

            curlv = nextlv

        # print("".join(res))
        return "".join(res)





    def serialize1(self, root: 'Node') -> str:
        if root == None: return ""

        serialized = []
        q = deque([root])
        while q:
            nextq = deque()
            while q:
                node = q.popleft()
                serialized.append("#" + str(node.val) + "@" + str(len(node.children)))
                
                for child in node.children:
                    nextq.append(child)
            q = nextq
        print("".join(serialized))
        return "".join(serialized)        

    def deserialize(self, data: str) -> 'Node':
        '''
        convert to [val, len of children]
        '''
        if data == "": return None

        deserializedData = data.split("#") # deserializedData[1:]
        deserializedData = deque([
            [int(val), int(numOfChildren)] 
            for valAndLen in deserializedData[1:]
            for val, numOfChildren in [valAndLen.split("@")]
        ])


        rootVal, rootChildLen = deserializedData.popleft()
        res = Node(rootVal)
        q = deque([[res, rootChildLen]])
        while q:
            
            nextq = deque()
            while q: # 32 20 40
                curNode, curChildLen = q.popleft()
                print(curNode.val, curChildLen)
                for _ in range(curChildLen):
                    val, childLen = deserializedData.popleft()
                    childNode = Node(int(val))

                    curNode.children.append(childNode)
                    nextq.append([childNode, childLen])

            q = nextq

        return res
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))







