'''
	Your task is to remove duplicates from given 
	sorted linked list.
	
	Function Arguments: head (head of the given linked list) 
	Return Type: none, just remove the duplicates from the list.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
#Function to remove duplicates from sorted linked list.
def removeDuplicates(head):
    #code here
    temp = head
    
    while temp != None and temp.next != None:
        if temp.data == temp.next.data:
            node = temp.next
            
            while node != None and node.data == temp.data:
                node = node.next
            
            temp.next = node
        
                
        temp = temp.next
        
    
    return head
    
    
    
    
    
        
        