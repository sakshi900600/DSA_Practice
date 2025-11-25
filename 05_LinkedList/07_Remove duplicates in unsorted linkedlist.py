'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	
'''
class Solution:
    #Function to remove duplicates from unsorted linked list.

    # it works but doesn't preserve the order of nodes
    def removeDuplicates(self, head):
        # code here
        # return head after editing list
        if head == None or head.next == None:
            return head
            
            
        s = set()
        
        temp = head
        
        while temp != None:
            s.add(temp.data)
            temp = temp.next
        
        
        dummy_node = Node(-1)
        temp = dummy_node
        
        for it in s:
            newNode = Node(it)
            temp.next = newNode
            temp = newNode
            
        
        return dummy_node.next
        
        
    def removeDuplicates_2(self, head):
        # code here
        # return head after editing list
        if head == None or head.next == None:
            return head
            
            
        s = set()
        
        temp = head
        s.add(temp.data)
        
        while temp is not None and temp.next is not None:
            if temp.next.data not in s:
                s.add(temp.next.data)
            else:
                node = temp.next
                
                while node is not None and node.data in s:
                    node = node.next

                temp.next = node
                

                if node != None:
                    s.add(node.data)
                
            temp = temp.next

        return head
        
        
        
        
        
        