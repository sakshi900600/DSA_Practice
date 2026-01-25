import heapq
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


class Solution:
    def mergeKLists(self, arr):
        # code here
        li = []
        
        for ll in arr:
            head = ll
            
            while head != None:
                li.append(head.data)
                head = head.next
        
        
        # print(li)
        li.sort()
        dummy = Node(-1)
        temp = dummy
        
        for data in li:
            newNode = Node(data)
            temp.next = newNode
            temp = newNode
        
        return dummy.next


    # using priority queue  
    def mergeKLists_pq(self, arr):
        # code here
        pq = []
        
        for ll in arr:
            head = ll
            
            while head != None:
                heapq.heappush(pq, head.data)
                head = head.next
        
        dummy = Node(-1)
        temp = dummy
            
        while pq:
            data = heapq.heappop(pq)
            newNode = Node(data)
            temp.next = newNode
            temp = newNode
        
        return dummy.next


    

        
            
            
if __name__ == "__main__":
    # Inputs: 
    list1 = Node(1)
    list1.next = Node(4)
    list1.next.next = Node(5)

    list2 = Node(1)
    list2.next = Node(3)
    list2.next.next = Node(4)

    list3 = Node(2)
    list3.next = Node(6)

    arr = [list1, list2, list3]

    sol = Solution()
    # merged_head = sol.mergeKLists(arr)
    merged_head = sol.mergeKLists_pq(arr)

    # Print merged linked list
    current = merged_head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
            
    # Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6 -> None


            
            