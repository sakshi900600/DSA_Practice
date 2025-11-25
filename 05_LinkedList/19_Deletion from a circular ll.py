'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    def deleteNode(self, head, key):
        #code here
        
        if head.next == head and head.data == key:
            head = None
            return head
        
        if head.data == key:
            temp = head
            
            while temp.next != head:
                temp = temp.next
            
            temp.next = head.next
            head = temp.next
                
            return head
            
            
        temp = head
        
        
        while temp.next != head and temp.next.data != key:
            temp = temp.next
        
        # key not found
        if temp.next.data != key:
            return head
            
        temp.next = temp.next.next
        
        return head
            
            
            