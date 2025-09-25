'''
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''

class Solution:
    def getKthFromLast(self, head, k):
        #code here
        
        length = 0
        temp = head
        while temp != None:
            length += 1
            temp = temp.next
            
        if k > length:
            return -1
        
        count = length - k 
        
        temp = head
        while count > 0:
            temp = temp.next
            count -= 1
        
        
        return temp.data
        
        
        