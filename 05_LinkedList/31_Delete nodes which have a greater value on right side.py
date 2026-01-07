
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None


class Solution:

    # tle:: 
    def compute(self,head):
        #Your code here
        
        temp = head
        
        while temp != None:
            node = temp.next
            while node != None:
                if node.data > temp.data:
                    temp.data = -1
                    break
                node = node.next
            
            temp = temp.next
            
        
        # get head
        if head.data == -1:
            temp = head
            while temp != None:
                if temp.data != -1:
                    head = temp
                    break
                temp = temp.next
        
        
        temp = head
        while temp != None:
            node = temp.next
            while node != None:
                if node.data != -1:
                    temp.next = node
                    break
                node = node.next
            
            temp = temp.next
        
        
        return head
        

    def compute2(self,head):
        #Your code here
        
        if head == None and head.next == None:
            return head
            
        # reverse ll so that we can properly check max val on right side.
        rev_head = self.reverse(head)
        max_val = rev_head.data 

        # for last node there will be no greater node on right side. so no need to think about the updated head.
        
        temp = rev_head
        while temp != None and temp.next != None:
            max_val = max(max_val, temp.data)
            
            if temp.next.data < max_val:
                node = temp.next
                while node != None and node.data < max_val:
                    node = node.next
                
                temp.next = node
            
            temp = temp.next
            
        
        final_head = self.reverse(rev_head)
        
        return final_head
        
        
    def reverse(self,head):
        if head == None and head.next == None:
            return head
        
        curr = head
        prev = None
        
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev
            
            
        
if __name__ == '__main__':
    head = Node(12)
    head.next = Node(15)
    head.next.next = Node(10)
    head.next.next.next = Node(11)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(2)
    head.next.next.next.next.next.next.next = Node(3)

    sol = Solution()
    new_head = sol.compute2(head)

    temp = new_head
    while temp != None:
        print(temp.data, end="->")
        temp = temp.next
        
    
    # Output: 15->11->6->3->