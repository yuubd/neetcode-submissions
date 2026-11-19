# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        while one of them is None:
            compare, if 1 = 2, => move the first one
            if 1 < 2, => 
                if 2 < 1.next => store 1.next in a tmp, attach 2 to 1.next and 2 become tmp

        return  1 || 2
        '''

        n1 = list1
        n2 = list2
        tmp = None
        while n1 and n2:
            print("start n1", self.printNode(n1), "n2", self.printNode(n2))
            
            if n1.val == n2.val: # 1135 25 134 
                tmp = n1.next
                n1.next = n2
                n2 = tmp 
                n1 = n1.next
            elif n1.val < n2.val:
                if not n1.next:
                    n1.next = n2
                    break
                elif n2.val <= n1.next.val:
                    tmp = n1.next
                    n1.next = n2
                    n2 = tmp
                n1 = n1.next
            else:
                if not n2.next:
                    n2.next = n1
                    break
                if n1.val <= n2.next.val:
                    tmp = n2.next
                    n2.next = n1
                    n1 = tmp
                n2 = n2.next

            print("end n1", self.printNode(n1), "n2", self.printNode(n2))
            print("list1", self.printNode(list1), "list2", self.printNode(list2), "\n")

        if not list1: return list2
        if not list2: return list1

        h1 = list1
        h2 = list2
        while True:
            if not list1: return h2
            if not list2: return h1
            list1 = list1.next
            list2 = list2.next
    
    def printNode(self, n):
        n_n = n
        s = ""
        while n_n:
            s += str(n_n.val)
            n_n = n_n.next
        return s







