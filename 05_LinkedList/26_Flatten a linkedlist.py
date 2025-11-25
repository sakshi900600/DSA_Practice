
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        


class Solution:
    def flatten(self, root):
        # code here
        
        head = root
        li = []
        
        while head != None:
            li.append(head.data)
            tail = head.bottom
            
            while tail != None:
                li.append(tail.data)
                tail = tail.bottom
            
            head = head.next
            
            
        li.sort()
        
        head = None
        tail = None
        
        for it in li:
            newNode = Node(it)
            if head == None:
                head = newNode
            else:
                tail.bottom = newNode
            tail = newNode
        
        
        return head
        
        
        
            