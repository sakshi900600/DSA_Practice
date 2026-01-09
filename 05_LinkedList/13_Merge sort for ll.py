
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# ------- very important  ------------
# here in mid finding fast starts from head.next not with head. See our goal is to divide the list in 2 approx equal parts.
# but in normal mid finding code we get the second mid and here we need first one why?

# ex - suppose ll = 1->2 in this case mid will be 2 but we want to divide it as 1 and 2 so that we can break the list into 2 parts.
# so to get first mid we start fast with head.next
# Crystal clear 👻

class Solution:
    def mergeSort(self, head):
        # code here
        if head == None or head.next == None:
            return head
        
        mid = self.getMid(head)

        right_head = mid.next
        mid.next = None
        
        new_left = self.mergeSort(head)
        new_right = self.mergeSort(right_head)
        
        return self.merge(new_left, new_right)
        
   
        
    
    def getMid(self, head):
        if head == None or head.next == None:
            return head
            
        slow = head
        fast = head.next
        
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            
        return slow
    
    
    def merge(self,head1, head2):
        
        if head1 == None and head2 == None:
            return None
        
        if head1 == None:
            return head2
        
        if head2 == None:
            return head1
            
        
        dummy = Node(-1)
        temp = dummy
        
        while head1 != None and head2 != None:
            if head1.data <= head2.data:
                temp.next = head1
                temp = head1
                head1 = head1.next
            else:
                temp.next = head2
                temp = head2
                head2 = head2.next
            
            
        while head1 != None:
            temp.next = head1
            temp = head1
            head1 = head1.next
        
        while head2 != None:
            temp.next = head2
            temp = head2
            head2 = head2.next
        
        return dummy.next
    



if __name__ == "__main__":
    head = Node(4)
    head.next = Node(2)
    head.next.next = Node(1)
    head.next.next.next = Node(3)

    sol = Solution()
    sorted_head = sol.mergeSort(head)

    # Print sorted linked list
    current = sorted_head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


        