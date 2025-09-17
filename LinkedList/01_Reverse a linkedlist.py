
class Solution:
    # iterative approach
    def reverseList(self, head):
        # Code here
        
        prev = None
        curr = head
        
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev
            
    
    # recursive
        
        


