class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = {} # key to node in the list
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1

        # link prev to n.next
        n = self.d[key]
        
        prev = n.prev
        next = n.next
        next.prev = prev
        prev.next = n.next

        # move n to head
        n.next = self.head.next
        n.prev = self.head
        self.head.next.prev = n
        self.head.next = n
        
        return self.head.next.val
        
    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d[key].val = value
            self.get(key)
            return

        if len(self.d) == self.capacity:
            # remove tail from d and linked list
            tailPrev = self.tail.prev
            del self.d[tailPrev.key]
            self.tail.prev = tailPrev.prev
            tailPrev.prev.next = self.tail
        
        # create and link the new node to the head and add to d
        newNode = Node(key, value)
        newNode.next = self.head.next
        newNode.prev = self.head
        self.head.next.prev = newNode
        self.head.next = newNode
        self.d[key] = newNode

        return

class Node:
    def __init__(self, key = 0, val = 0, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
