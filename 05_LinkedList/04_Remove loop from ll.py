
class Node:
    def __init__(self,val):
        self.next=None
        self.data=val


class Solution:
    def removeLoop(self, head):
        # code here
        # step1 - check if cycle exists, 
        # step2 - if not return as it is
        # step3 - otherwise find the first node in loop and at the same time keep track of last node and at last do last node.next = none
        
        slow = head
        fast = head
        isCycle = False
        
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                isCycle = True
                break
        
        if isCycle == False:
            return head
        
        # if loop on head
        if slow == head:
            
            tail = head.next
            while tail.next != head:
                tail = tail.next
            
            tail.next = None
            return head
        
        
        # step 3
        slow = head
        prev = None
        
        while slow != fast:
            prev = fast
            slow = slow.next
            fast = fast.next
        
        
        prev.next = None
        
        return head
        
        
        
        
if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = head.next.next  # Creating a loop for testing

    sol = Solution()
    sol.removeLoop(head)

    # Print the linked list after removing the loop
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
            
            