# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        None => None
        1 2, if k > len of the nodes, do nothing
        1 2, if k <= len of the nodes, reverse
        
        1 > 2 > 3
        1 < 2 < 3
        res > 3 > 2 > 1 > 4 ...
        if the next nodes < k then it s the end. return the res?

        res > 3 > 2 > 1 >   4 > 5 > 6 ..
                  tail^ head^ >>>>>>^
        when at the tail, save the next as tmp
        and tail.next is new tail before assigning

        states
            counter = k and reset for next search
            res = ListNode(-1)
            
            head of the k nodes, = None in the beginning
            tail of the k nodes = res in the beginning
            while True:
                find the next head and tail
                n
                while the count > 0 or n is not none:
                    move n >>
                if n is none:
                    return break
                if n is not None:
                    tail.next = n
                tail = n
                save tmp = tail.next #tmp=4 # 1>2>3
                while tail != head:
                    reverse the node # 3>2>1, tail is 1 and head is 1 res >3
                head = tmp 3 tail=1                
                
            return the res
        ''' 
        res = ListNode(-1)
        res.next = head
        
        head = head
        tail = res
        
        n = head
        while True:
            count = k 
            # print("@@ n.val", n.val) # 3, 6
            while count-1 > 0 and n is not None:
                n = n.next
                count -= 1
            
            
            if n == None:
                break
            
            tail.next = n # res > 3
            tail = n # tail = 3
            tmpNewHead = tail.next # 4
            # print("n.val", n.val) # 3, 6

            tmpHead = head
            prev = tmpNewHead
            # print(tmpNewHead.val if tmpNewHead else -1 , head.val, tail.val) # 4 1 3
            while tmpHead != tmpNewHead:
                tmp = tmpHead.next # 
                tmpHead.next = prev # 2>
                
                # print(
                #     "@@ reverse \n",
                #     "prev", prev.val if prev else -1,
                #     "tmpHead", tmpHead.val if tmpHead else -1,
                #     "tmpHead.next", tmpHead.next.val if tmpHead and tmpHead.next else -1,
                #     "tmp", tmp.val if tmp else -1
                # ) # 1 2 3 4 5 6
                prev = tmpHead
                tmpHead = tmp
            # a = res
            # t = []
            # while a:    
            #     t.append(str(a.val))
            #     a = a.next
            # print("".join(t))
            tail = head
            head = tmpNewHead
            n = tmpNewHead
            # print(
            #     "head", head.val if head else -1,
            #     "tail", tail.val if tail else -1,
            # )
            
            
                
        return res.next














