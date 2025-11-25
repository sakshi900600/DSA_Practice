# User function Template for Python3

# Following is the structure of node 
# class node:
#     def __init__(self):  
#         self.data = None
#         self.next = None

class Solution:
    def divide(self, head):
        # code here
        
        evenHead = None
        oddHead = None
        
        temp = head
        while temp != None:
            if temp.data % 2 == 0:
                if evenHead == None:
                    evenHead = temp
                    even = evenHead
                else:
                    even.next = temp
                    even = temp
            else:
                if oddHead == None:
                    oddHead = temp
                    odd = oddHead
                else:
                    odd.next = temp
                    odd = temp
            
            temp = temp.next
            
        
        if evenHead == None:
            return oddHead
            
        even.next = oddHead
        
        if oddHead:
            odd.next = None
        
        return evenHead
        
        