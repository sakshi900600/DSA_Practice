class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Solution:
    # iterative approach
    def reverseList(self, head):
        # Code here
        
        prev = None
        curr = head
        
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev
            

    
    # recursive
    def reverse_rec(self, head):
        if head == None or head.next == None:
            return head
        
        new_head = self.reverse_rec(head.next)
        # reverse the head at last
        head.next.next = head
        head.next = None

        return new_head

    

if __name__ == "__main__":

    # input
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    sol = Solution()
    # rev_head = sol.reverseList(head)
    rev_head = sol.reverse_rec(head)

    while rev_head != None:
        print(rev_head.data, end="->")
        rev_head = rev_head.next

    

        
        


