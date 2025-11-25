
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def intersectPoint(self, head1, head2):
        # code here
        
        temp1 = head1
        temp2 = head2
        
        while temp1 != temp2:
            
            if temp1 == None:
                temp1 = head2
            else:
                temp1 = temp1.next
            
            if temp2 == None:
                temp2 = head1
            else:
                temp2 = temp2.next
                
        
        return temp1
                
                
                
                
                
                
        