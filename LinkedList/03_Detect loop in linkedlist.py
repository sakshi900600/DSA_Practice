'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def detectLoop(self, head):
        # code here
        
        slow = head
        fast = head
        
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
                
        
        return False
        
        
