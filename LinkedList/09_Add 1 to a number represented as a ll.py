'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    def addOne(self,head):
        #Returns new head of linked List.
        
        if head == None:
            return head
        
        rev_head = self.reverse(head)
        
        first_node = rev_head
        updated_val = first_node.data + 1
        value = updated_val % 10
        carry = updated_val // 10
        
        first_node.data = value
        
        # step 2
        temp = rev_head.next
        
        while temp != None:
            updated_val = temp.data + carry
            temp.data = updated_val % 10
            carry = updated_val // 10
            
            temp = temp.next
        
        
        new_head = self.reverse(rev_head)
        
        # if carray lefts
        if carry != 0:
            newNode = Node(carry)
            newNode.next = new_head
            new_head = newNode
        
        
        
        return new_head
        
    
    
    def reverse(self,head):
        if head == None or head.next == None:
            return head
            
        prev = None
        
        curr = head
        
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            
        return prev
        
        