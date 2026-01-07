import heapq

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        


class Solution:
    def flatten(self, root):
        # code here
        
        head = root
        li = []
        
        while head != None:
            li.append(head.data)
            tail = head.bottom
            
            while tail != None:
                li.append(tail.data)
                tail = tail.bottom
            
            head = head.next
            
            
        li.sort()
        
        head = None
        tail = None
        
        for it in li:
            newNode = Node(it)
            if head == None:
                head = newNode
            else:
                tail.bottom = newNode
            tail = newNode
        
        
        return head
        
        
    def flatten2(self, root):
        # code here
        
        pq = []
        temp = root
        
        while temp != None:
            next_node = temp.next
            
            while temp != None:
                heapq.heappush(pq, temp.data)
                temp = temp.bottom
            temp = next_node
            
        # print(pq)
        dummy = Node(-1)
        temp = dummy
        
        
        while len(pq) > 0:
            data = heapq.heappop(pq)
            # print(data)
            newNode = Node(data)
            temp.bottom = newNode
            temp = newNode
        
        return dummy.bottom
        
        

if __name__ == "__main__":
    # input
    head = Node(5)
    head.next = Node(10)
    head.next.next = Node(19)
    head.next.next.next = Node(28)

    head.bottom = Node(7)
    head.bottom.bottom = Node(8)

    head.next.bottom = Node(20)

    head.next.next.bottom = Node(22)

    head.next.next.next.bottom = Node(40)
    head.next.next.next.bottom.bottom = Node(45)

    sol = Solution()
    new_head = sol.flatten(head)
    # new_head = sol.flatten2(head)


    while new_head != None:
        print(new_head.data , end="->")
        new_head = new_head.bottom
    

    # Ouput: 5->7->8->10->19->20->22->28->40->45->

            