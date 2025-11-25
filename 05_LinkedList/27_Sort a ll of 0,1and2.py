'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
	
class Solution:

    def segregate(self, head):
        #code here
        
        temp = head
        c0 = 0
        c1 = 0
        c2 = 0
        
        while temp != None:
            if temp.data == 0:
                c0 += 1
            elif temp.data == 1:
                c1 += 1
            else:
                c2 += 1
            
            temp = temp.next
        
        
        temp = head
        while temp != None:
            if c0 > 0:
                temp.data = 0
                c0 -= 1
            elif c1 > 0:
                temp.data = 1
                c1 -= 1
            else:
                temp.data = 2
                c2 -= 1
            
            temp = temp.next
        
        return head
            

    def segregate2(self, head):
        #code here
        
        zeroHead = Node(-1)
        oneHead = Node(-1)
        twoHead = Node(-1)
        
        zero = zeroHead
        one = oneHead
        two = twoHead
        
        
        temp = head
        
        while temp != None:
            if temp.data == 0:
                zero.next = temp
                zero = temp
            elif temp.data == 1:
                one.next = temp
                one = temp
            else:
                two.next = temp
                two = temp
            
            temp = temp.next
        
        
        
        # connect
        if oneHead.next != None:
            zero.next = oneHead.next
        else:
            zero.next = twoHead.next
        
        
        one.next = twoHead.next
        two.next = None
        
        return zeroHead.next
             
            
    
            
            
            