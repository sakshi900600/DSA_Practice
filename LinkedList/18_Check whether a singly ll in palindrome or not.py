
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



class Solution:
    def isPalindrome(self, head):
        # code here
        slow = head
        fast = head
        
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        head2 = self.reverse(slow)
        temp1 = head
        temp2 = head2
        
        while temp2 != None:
            if temp1.data != temp2.data:
                return False
            
            temp1 = temp1.next
            temp2 = temp2.next
            
        
        return True
        
        
    
    def reverse(self,head):
        prev = None
        
        curr = head
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev
        
        