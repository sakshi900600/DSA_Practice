'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    def deleteNode(self, head, key):
        #code here
        if head==None:
            return head
        
        tail = head.next
        while tail.next != head:
            tail = tail.next
        
        if head.data == key:
            head = head.next
            tail.next = head
            return head
        
        temp = head
        while temp.next != head:
            if temp.next.data == key:
                temp.next = temp.next.next
                break
            temp = temp.next
        
        return head
        
        
        
            
        