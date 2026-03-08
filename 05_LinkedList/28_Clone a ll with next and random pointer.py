
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
        self.random = None
     

class Solution:
    def cloneLinkedList(self, head):
        # code here
        
        dct = {}
        
        temp = head
        while temp != None:
            dup_node = Node(temp.data)
            dct[temp] = dup_node
            temp = temp.next
        
        
        temp = head
        while temp != None:
            dup_node = dct.get(temp)
            dup_node.next = dct.get(temp.next)
            dup_node.random = dct.get(temp.random)
            temp = temp.next
            
        return dct.get(head)
        
        

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.random = head.next.next
    head.next.random = head
    head.next.next.random = head.next
    
    sol = Solution()
    dup_head = sol.cloneLinkedList(head)
    
    # Print the original and cloned linked list to verify
    temp = head
    while temp:
        print(f"Original Node: {temp.data}, Random: {temp.random.data if temp.random else None}")
        temp = temp.next
        
    temp = dup_head
    while temp:
        print(f"Cloned Node: {temp.data}, Random: {temp.random.data if temp.random else None}")
        temp = temp.next
