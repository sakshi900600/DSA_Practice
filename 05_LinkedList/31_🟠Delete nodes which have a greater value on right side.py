
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None


class Solution:

    # tle:: 
    def compute(self,head):
        #Your code here
        
        temp = head
        
        while temp != None:
            node = temp.next
            while node != None:
                if node.data > temp.data:
                    temp.data = -1
                    break
                node = node.next
            
            temp = temp.next
            
        
        # get head
        if head.data == -1:
            temp = head
            while temp != None:
                if temp.data != -1:
                    head = temp
                    break
                temp = temp.next
        
        
        temp = head
        while temp != None:
            node = temp.next
            while node != None:
                if node.data != -1:
                    temp.next = node
                    break
                node = node.next
            
            temp = temp.next
        
        
        return head
        
                
            
        
        