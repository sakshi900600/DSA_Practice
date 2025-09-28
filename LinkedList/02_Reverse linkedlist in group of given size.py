"""
class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
"""

class Solution:
    def reverseKGroup(self, head, k):
        # Code here
        
        if not head or k == 1:
            return head
            
            
        temp = head
        prevNode = None
        
        while temp != None:
            kthNode = self.getKthNode(temp,k)
            
            if kthNode == None:
                if prevNode != None:
                    prevNode.next = self.reverse(temp)
                    break
            
            else:
                nextNode = kthNode.next
                kthNode.next = None
                
                self.reverse(temp)
                
                if temp == head:
                    head = kthNode
                else:
                    prevNode.next = kthNode
                
                prevNode = temp
                temp = nextNode
                
        
        return head
        
    
    
    def getKthNode(self,head,k):
        k -= 1
        while head != None and k > 0:
            k -= 1
            head = head.next
            
        return head
        
        
    
    def reverse(self,head):
        curr = head
        prev = None
        
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev
        
        