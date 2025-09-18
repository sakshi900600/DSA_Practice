class Solution:
    def moveToFront(self, head : Optional['Node']) -> Optional['Node']:
        # code here
        
        temp = head
        sec_last = None
        while temp.next != None:
            sec_last = temp
            temp = temp.next
        
        sec_last.next = None
        temp.next = head
        head = temp
        
        
        return head
        
        
        
        
