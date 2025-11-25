
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
            
            
            
        
        
        
        