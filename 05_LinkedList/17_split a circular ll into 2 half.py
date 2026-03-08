
class Node:
    def __init__(self):
        self.data = None
        self.next = None



class Solution:
    def splitList(self, head):
        #code here
        
        temp = head.next
        length = 1
        
        while temp != head:
            length += 1
            temp = temp.next
        
        
        if length % 2 == 0:
            mid = length // 2
        else:
            mid = length//2 + 1
        
        half = mid
        
        temp = head
        while True:
            mid -= 1
            
            if mid == 0:
                right_head = temp.next
                break
            temp = temp.next
        
        temp.next = head
        
        
        temp = right_head
        last = length - half
        
        if right_head != None:
        
            while True:
                last -= 1
                if last == 0:
                    break
                
                temp = temp.next
            
            temp.next = right_head
        
        
        return (head, right_head)


    def splitList_easy(self, head):
        #code here
        # step1: find mid node and tail
        # step2: store mid.next as h2 and connect mid to the head and tail to the h2
        tail = head.next
        while tail.next != head:
            tail = tail.next
        
        mid = self.getmid(head)
        sech = mid.next
        mid.next = head
        
        tail.next = sech
        
        return [head, sech]
        
    
    # this getmid is written for circular ll.
    def getmid(self, head):
        slow = head
        fast = head.next
        while fast != head and fast.next != head:
            slow = slow.next
            fast = fast.next.next
        
        return slow    
            
            
if __name__ == "__main__":
    head = Node()
    head.data = 1
    head.next = Node()
    head.next.data = 2
    head.next.next = Node()
    head.next.next.data = 3
    head.next.next.next = Node()
    head.next.next.next.data = 4
    head.next.next.next.next = head
    
    sol = Solution()
    h1, h2 = sol.splitList(head)
    
    # Print the two halves to verify
    temp = h1
    while True:
        print(temp.data, end=" ")
        temp = temp.next
        if temp == h1:
            break
    print()
    
    temp = h2
    while True:
        print(temp.data, end=" ")
        temp = temp.next
        if temp == h2:
            break

        