
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def addTwoLists(self, head1, head2):
        # code here
        rh1 = self.reverse(head1)
        rh2 = self.reverse(head2)
        
        temp1 = rh1
        temp2 = rh2
        dummy = Node(-1)
        temp = dummy
        
        carry = 0
        
        
        while temp1 != None or temp2 != None:
            v1 = temp1.data if temp1 else 0
            v2 = temp2.data if temp2 else 0
            value = v1+v2+carry
            
            newNode = Node(value % 10)
            temp.next = newNode
            temp = newNode
            
            carry = value // 10
            
            
            if temp1:
                temp1 = temp1.next
            if temp2:
                temp2 = temp2.next
            
        
        if carry != 0:
            newNode = Node(carry)
            temp.next = newNode
        
        
        newHead = self.reverse(dummy.next)
        
        node = newHead
        while node != None and node.data == 0 and node.next != None:
            node = node.next
        
        return node
        
        
    
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
        
        