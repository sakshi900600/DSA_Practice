class Solution:
    def rotateDLL(self, head, p):
        # Code here..
        
        if head == None or head.next == None or p==0:
            return head
        
        
        length = 1
        tail = head
        while tail.next != None:
            tail = tail.next
            length += 1
        
        
        p = p % length
        if p == 0:
            return head # coz indexing start with 1
        
        
        temp = head
        for i in range(p-1):
            temp = temp.next
        
        
        next_head = temp.next
        temp.next = None
        next_head.prev = None
        
        # connect tail with head
        tail.next = head
        head.prev = tail
        
        
        return next_head
        
        
        