
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


class Solution:
    def reverse(self, head):
        # code here
        
        prev = None
        curr = head
        
        while curr != None:
            next = curr.next
            curr.next = curr.prev
            curr.prev = next
            prev = curr
            curr = next
        
        
        return prev
        