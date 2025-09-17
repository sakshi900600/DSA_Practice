"""
class Node:
    def __init__(self, data):   
        self.data = data
        self.next = None
"""

class Solution:
    def cycleStart(self, head):
        #code here
        
        slow = head
        fast = head
        
        cycle = False
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                cycle = True
                break
            
        if cycle == True:    
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            
            return slow.data
        else:
            return -1
            
        
        
        