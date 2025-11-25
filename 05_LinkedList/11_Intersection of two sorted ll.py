
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None



class Solution:
    def findIntersection(self,head1,head2):
        #return head
        
        temp1 = head1
        temp2 = head2
        dummy = Node(-1)
        temp = dummy
        
        while temp1 != None and temp2 != None:
            if temp1.data == temp2.data:
                newNode = Node(temp1.data)
                temp.next = newNode
                temp = newNode
                
                temp1 = temp1.next
                temp2 = temp2.next
            elif temp1.data < temp2.data:
                temp1 = temp1.next
            else:
                temp2 = temp2.next
          
              
        return dummy.next
        
        
                
                
                